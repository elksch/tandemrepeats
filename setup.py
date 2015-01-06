from distutils.core import setup

setup(
    name='tandemrepeats',
    version='0.3.0',
    author='Elke Schaper',
    author_email='elke.schaper@isb-sib.ch',
    packages=['hmm', 'hmm.test', 'repeat', 'repeat.test', 'repeat_list', 'repeat_list.test', 'sequence', 'sequence.test'],
    scripts=['scripts/detect_tandem_repeats_in_sequence', 'scripts/example_pipeline'],
    url='http://pypi.python.org/pypi/tandemrepeats/',
    license='LICENSE.txt',
    description='Detect and evaluate tandem repeats in genomic sequence data.',
    long_description=open('README.markdown').read(),
    classifiers = [
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS"
        ],
    install_requires=[
        "argparse >= 1.2.1",
        "Biopython >= 1.64",
        "configobj >= 5.0.6",
        "docutils >= 0.11",
        "numpy >= 1.6.1",
        "pytest >= 2.5.2",
        "scipy >=0.12.0",
        "setuptools >= 5.1",
        "Sphinx >= 1.2.2",
    ],
    package_data={'tandemrepeats': ['data/*']},
    package_dir={'tandemrepeats': 'tandemrepeats'},
)
