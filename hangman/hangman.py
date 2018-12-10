import random
import argparse


def make_dictionary_from_file(dict_path):
    dictionary = None
    try:
        with open(dict_path, "r") as dict_f:
            dictionary = [word.strip() for word in dict_f.readlines()]
    except IOError:
        print("Incorrect path to dictionary file!")

    return dictionary if dictionary is not None else []


class HangmanGame:
    current_word = None
    current_answer = None
    max_mistakes = 5
    mistakes_counter = 0
    used_letters = set()
    win = False

    def __init__(self, word, max_mistakes=None):
        """
        :type word: str
        :type max_mistakes: int | None
        """
        self.current_word = word
        if max_mistakes:
            self.max_mistakes = max_mistakes

    @staticmethod
    def get_next_letter():
        """
        :rtype: char
        """
        print("Guess a letter:")
        next_letter = input().strip()
        while not len(next_letter) == 1:
            print("Type only 1 symbol!")
            next_letter = input().strip()
        return next_letter

    def do_step(self, next_letter):
        """
        :type next_letter: char
        :rtype: bool
        """
        if "*" not in self.current_answer:
            print("You won!")
            return True
        if next_letter in self.used_letters:
            print("This letter has already been used")
        else:
            if next_letter in self.current_word:
                print("Hit!")
                for i in range(len(self.current_word)):
                    if self.current_word[i] == next_letter:
                        self.current_answer[i] = next_letter
                print("The word:", self.current_answer)
            else:
                self.mistakes_counter += 1
                print("Missed, mistake {} out of {}."
                      .format(self.mistakes_counter, self.max_mistakes))
        return False

    def start_game(self):
        self.current_answer = ["*" for _ in range(len(self.current_word))]
        self.mistakes_counter = 0
        won = False

        while self.mistakes_counter < self.max_mistakes and not won:
            won = self.do_step(self.get_next_letter())

        if not won:
            print("You lost!")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mistakes",
                        help="maximum number of mistakes",
                        default=5, required=False)
    parser.add_argument("--dictionary", help="path to dictionary",
                        required=False)
    args = parser.parse_args()
    dictionary_path = None
    if args.dictionary:
        dictionary_path = args.dictionary
    dictionary = make_dictionary_from_file(dictionary_path)
    assert dictionary, "Dictionary must not be empty!"
    word = random.choice(dictionary)
    new_game = HangmanGame(max_mistakes=args.mistakes, word=word)
    new_game.start_game()


if __name__ == "__main__":
    main()
