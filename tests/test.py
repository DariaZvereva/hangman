from hangman.hangman import make_dictionary_from_file


def test_make_dictionary_from_file():
    dictionary = make_dictionary_from_file(
        dict_path="hangman/data/dictionary"
    )
    assert dictionary == ["programming", "fintech", "student"]
