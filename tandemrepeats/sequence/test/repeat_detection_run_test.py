import logging
import os
import pytest

from tandemrepeats.sequence import repeat_detection_run, sequence

TEST_SEQUENCE_Q9BRR0 = "MARELSESTALDAQSTEDQMELLVIKVEEEEAGFPSSPDLGSEGSRERFRGFRYPEAAGPREALSRLRELCRQWLQPEMHSKEQILELLVLEQFLTILPGNLQSWVREQHPESGEEVVVLLEYLERQLDEPAPQVSGVDQGQELLCCKMALLTPAPGSQSSQFQLMKALLKHESVGSQPLQDRVLQVPVLAHGGCCREDKVVASRLTPESQGLLKVEDVALTLTPEWTQQDSSQGNLCRDEKQENHGSLVSLGDEKQTKSRDLPPAEELPEKEHGKISCHLREDIAQIPTCAEAGEQEGRLQRKQKNATGGRRHICHECGKSFAQSSGLSKHRRIHTGEKPYECEECGKAFIGSSALVIHQRVHTGEKPYECEECGKAFSHSSDLIKHQRTHTGEKPYECDDCGKTFSQSCSLLEHHRIHTGEKPYQCSMCGKAFRRSSHLLRHQRIHTGDKNVQEPEQGEAWKSRMESQLENVETPMSYKCNECERSFTQNTGLIEHQKIHTGEKPYQCNACGKGFTRISYLVQHQRSHVGKNILSQ"
TEST_FINDERS = ["TREKS", "TRUST", "XSTREAM"]

notfixed = pytest.mark.notfixed

#@notfixed
def test_detect_denovo():

    test_seq = sequence.Sequence(TEST_SEQUENCE_Q9BRR0)
    predicted_repeats = repeat_detection_run.run_TRD(seq_records = [test_seq], lFinders = TEST_FINDERS)
    assert len(predicted_repeats) == 1
    assert len(predicted_repeats[0]) == 3
    # Include better tests here!
