import random
import argparse


class HangmanGame(object):
    dictionary = None
    current_word = None
    current_answer = None
    max_mistakes = 5
    mistakes_counter = 0
    used_letters = set()
    win = False

    def __init__(self,
                 dict_path=None,
                 max_mistakes=None):
        if max_mistakes:
            self.max_mistakes = max_mistakes
        if dict_path:
            self.make_dictionary_from_file(dict_path)
        else:
            self.dictionary = ["forest", "mother", "abracadabra"]

    def make_dictionary_from_file(self, dict_path):
        try:
            dict_f = open(dict_path, "r")
            self.dictionary = [word.strip() for word in dict_f.readlines()]
        except IOError:
            print "Incorrect path to dictionary file!"

    @staticmethod
    def get_next_letter():
        print "Guess a letter:"
        next_letter = raw_input()
        while not len(next_letter) == 1:
            print "Type only 1 symbol!"
            next_letter = input().strip()
        return next_letter

    def do_step(self, next_letter):
        if "*" not in self.current_answer:
            print "You won!"
            return True
        if next_letter in self.used_letters:
            print "This letter has already been used"
        else:
            if next_letter in self.current_word:
                print "Hit!"
                for i in range(len(self.current_word)):
                    if self.current_word[i] == next_letter:
                        self.current_answer[i] = next_letter
                print "The word:", self.current_answer
            else:
                self.mistakes_counter += 1
                print "Missed, mistake {} out of {}." \
                    .format(self.mistakes_counter, self.max_mistakes)
        return False

    def start_game(self):
        self.current_word = random.choice(self.dictionary)
        self.current_answer = ["*" for _ in range(len(self.current_word))]
        self.mistakes_counter = 0
        won = False
        while self.mistakes_counter < self.max_mistakes and not won:
            won = self.do_step(self.get_next_letter())

        if not won:
            print "You lost!"


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("--mistakes",
                        help="maximum number of mistakes",
                        default=5, required=False)
    PARSER.add_argument("--dictionary", help="path to dictionary",
                        required=False)
    ARGS = PARSER.parse_args()
    DICTIONARY_PATH = None
    if ARGS.dictionary:
        DICTIONARY_PATH = ARGS.dictionary
    NEW_GAME = HangmanGame(max_mistakes=ARGS.mistakes,
                           dict_path=DICTIONARY_PATH)
    NEW_GAME.start_game()
