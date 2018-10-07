import random
import argparse


class hangman_game(object):
    dictionary = None
    current_word = None
    current_answer = None
    MAX_MISTAKES = 5
    mistakes_counter = 0
    used_letters = set()
    win = False

    def __init__(self,
                 dict_path=None,
                 max_mistakes=None):
        if max_mistakes:
            self.MAX_MISTAKES = max_mistakes
        if dict_path:
            self.make_dictionary_from_file(dict_path)
        else:
            self.dictionary = ["forest", "mother", "abracadabra"]

    def make_dictionary_from_file(self, dict_path):
        try:
            dict_f = open(dict_path, "r")
            self.dictionary = [word.strip() for word in dict_f.readlines()]
        except:
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
                print("Hit!")
                for i in range(len(self.current_word)):
                    if self.current_word[i] == next_letter:
                        self.current_answer[i] = next_letter
                print "The word:", self.current_answer
            else:
                self.mistakes_counter += 1
                print "Missed, mistake {} out of {}.".format(self.mistakes_counter, self.MAX_MISTAKES)
        return False

    def start_game(self):
        self.current_word = random.choice(self.dictionary)
        self.current_answer = ["*" for _ in range(len(self.current_word))]
        self.mistakes_counter = 0
        won = False
        while self.mistakes_counter < self.MAX_MISTAKES and not won:
            won = self.do_step(self.get_next_letter())

        if not won:
            print "You lost!"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mistakes", type=int, help="maximum number of mistakes", default=5, required=False)
    parser.add_argument("--dictionary", help="path to dictionary", required=False)
    args = parser.parse_args()
    if args.dictionary:
        dictionary_path = args.dictionary
    else:
        dictionary_path = None
    new_game = hangman_game(max_mistakes=args.mistakes, dict_path=dictionary_path)
    new_game.start_game()
