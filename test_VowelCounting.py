import pytest
import VowelCounting

# check the ordinary vowel counting methods

def test_for_vowel_a():
    vowel_counter = VowelCounter("Some string")
    assert(True, vowel_counter.check_for_vowel('a') == -1)

def test_for_vowel_b():
    vowel_counter = VowelCounter("Some string")
    assert(True, vowel_counter.check_for_vowel('b') == 0)


# def test_for_y_vowel_g():
#     vowel_counter = VowelCounter("Some string")
#     assert(True, vowel_counter.check_for_y_vowel("gym",0) == 0)