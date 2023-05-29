import os
import tempfile

import hangman

import pytest

# Tests for get_random_word

def test_select_random_word_min_length():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["cat\n","elephant\n","mouse\n","dog\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman.get_random_word(name)
        assert secret_word == "elephant"

    os.unlink(name)

def test_select_random_word_no_non_alpha_chars():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["pine's\n","Dr.\n","Ångström\n","policeman\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman.get_random_word(name)
        assert secret_word == "policeman"

    os.unlink(name)

def test_select_random_word_no_capitals():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["Alexander\n","AMD\n","California\n","pelican\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman.get_random_word(name)
        assert secret_word == "pelican"

    os.unlink(name)


def test_select_random_word_no_repetitions():
    secret_words = set()
    for _ in range(10):
        secret_words.add(hangman.get_random_word())
    assert len(secret_words) == 10
    
##

# Tests for get_partial_solution 

def test_partial_solution_normal_input():
    assert hangman.get_partial_solution("pineapples") == "__________"

##

# Tests for display_hangman

def test_display_hangman_normal_input():
    assert hangman.display_hangman(4) == """+---,
|   o
|  /|
|
^"""

def test_display_hangman_out_of_bounds():
    with pytest.raises(IndexError):
        hangman.display_hangman(-10)

##

# Tests for display_word_and_guesses

def test_display_word_and_guesses_normal_input():
    assert hangman.display_word_and_guesses("_______", ['p', 'e']) == "Mystery Word = _______, Wrong Guesses = ['p', 'e']"

def test_display_word_and_guesses_empty_guess():
    assert hangman.display_word_and_guesses("_________", []) == "Mystery Word = _________, Wrong Guesses = []"