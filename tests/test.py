from hangman import HangmanGame


def test_make_dictionary_from_file():
    game = HangmanGame(dict_path="../hangman/data/dictionary")
    assert game.dictionary == ["programming", "fintech", "student"]


def test_do_step():
    game = HangmanGame()
    game.current_word = "abc"
    game.current_answer = ["a", "*", "*"]
    assert not game.do_step("b")
    assert game.current_answer == ["a", "b", "*"]
    assert not game.do_step("t")
    assert game.current_answer == ["a", "b", "*"]
