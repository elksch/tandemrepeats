# (C) 2014-2015 Elke Schaper

"""
    :synopsis: Access TRAL configuration files

    .. moduleauthor:: Elke Schaper <elke.schaper@isb-sib.ch>
"""

import os
import shutil
import urllib.request as request
from contextlib import closing

# Where are the executables stored? E.g. the tandem repeat detection
# algorithms?
EXEC_DIR = "/usr/local/bin"

# What is the path to the package? E.g. path/to/Tral/tral
PACKAGE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# The default location of the local config files
CONFIG_DIR = os.path.join(os.path.expanduser('~'), ".tral")

# Where are the data-files, e.g. for pvalue calculation stored?
DATA_DIR = os.path.join(CONFIG_DIR, "data")

# URL to download missing config files. If None, don't try to download
# Corresponds to DATA_DIR contents
CONFIG_DATA_URL = "ftp://ftp.vital-it.ch/papers/vital-it/Bioinformatics-Schaper/"


def config_file(name, config_dir=CONFIG_DIR, config_url=CONFIG_DATA_URL):
    '''Returns the complete path to the config file `name`.

    Returns the complete path to the config file `name`.

    Search path:
        - CONFIG_DIR (~/.tral)
        - Default files within the tral distribution (PACKAGE_DIRECTORY/tral_configuration/)
            - .ini files will be copied to CONFIG_DIR
        - Download from CONFIG_DATA_URL

    Args:
      - name (str): path to the requested file relative to config_dir. Should be slash-separated (even on windows)
      - config_dir (str): Override CONFIG_DIR (for testing)
      - url (str): Override download url (for testing)
    '''
    # Minimum file size; used to detect download errors
    MIN_FILE_SIZE = 0

    # Config dir
    user_path = os.path.join(config_dir, name)
    if os.path.isfile(user_path):
        return user_path

    # Package
    path = os.path.join(PACKAGE_DIRECTORY, 'tral_configuration', name)
    if os.path.isfile(path):
        # Copy to config_dir
        shutil.copyfile(path, user_path)
        return user_path

    # Download
    path = os.path.join(config_dir, name)
    url = config_url + name
    download(url, path)
    if os.path.isfile(path) and os.path.getsize(path) > MIN_FILE_SIZE:
        return path
    else:
        raise FileNotFoundError("Error downloading %s" % url)

    # Give up
    raise ValueError("Unknown configuration file: %s" % name)


def download(url, path):
    """Download a url to a file. Overwrites destination if present."""

    with closing(request.urlopen(url)) as r:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as f:
            shutil.copyfileobj(r, f)
