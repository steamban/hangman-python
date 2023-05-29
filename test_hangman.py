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

##

# Tests for update_masked_word

def test_update_masked_word_no_guesses():
    assert hangman.update_masked_word("hangman", "_______") == ("_______", [' '])

def test_update_masked_word_wrong_guesses():
    assert hangman.update_masked_word("hangman", "______n", 'p', ['y', 'u']) == ("______n", ['y', 'u', 'p'])

def test_update_masked_word_correct_guesses_multiple_positions():
    assert hangman.update_masked_word("hangman", "h__gm__", 'a', ['y', 'u']) == ("ha_gma_", ['y', 'u'])

def test_update_masked_word_correct_guess():
    assert hangman.update_masked_word("hangman", "ha__ma_", 'g', ['y', 'u']) == ("ha_gma_", ['y', 'u'])

def test_update_masked_word_repeated_guess():
    assert hangman.update_masked_word("hangman", "ha_gma_", 'g', ['y', 'u']) == ("ha_gma_", ['y', 'u'])

##

# Tests for check_game_over 

def test_check_game_over_win():
    assert hangman.check_game_over('hangman', 'hangman') == 'You Win!';

def test_check_game_over_lose():
    assert hangman.check_game_over('hangman', '_angman') == 'You Lose!, the Mystery Word was -> hangman'

##

# Tests for check_game_loop

def test_check_game_loop_next_turn():
    assert hangman.check_game_loop('_angman', 'hangman', ['z', 'y']) == True

def test_check_game_loop_win():
    assert hangman.check_game_loop('hangman', 'hangman', ['z', ]) == False

def test_check_game_loop_empty_wrong_guess():
    assert hangman.check_game_loop('hangman', 'hangman') == False

def test_check_game_loop_out_of_turns():
    assert hangman.check_game_loop('_ang_an', 'hangman', ['z', 'x', 'o', 'r', 'l', 'k', 'y']) == False

##

# Tests display_game_status()