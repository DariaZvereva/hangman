import mock

from hangman.hangman import hangman_game


def test_make_dictionary_from_file():
    game = hangman_game(dict_path="../hangman/data/dictionary")
    assert game.dictionary == ["programming", "fintech", "student"]


def test_do_step():
    game = hangman_game()
    game.current_word = "abc"
    game.current_answer = ["a", "*", "*"]
    assert not game.do_step("b")
    assert game.current_answer == ["a", "b", "*"]
    assert not game.do_step("t")
    assert game.current_answer == ["a", "b", "*"]
