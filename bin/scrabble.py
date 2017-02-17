class Scrabble(object):
    """
    List all possible words, and theirs score if score=True, else returns
    words lengths, comprised of entered letters as a string.
    Optional: obligatory letters - letters which must be used.

    types:
    letters: str
    obligatory: str
    score: boolean
    """

    def __init__(self):
        self.letters = ''
        self.obligatory = ''
        self.score = True
        self.words = []
        self.word_scores = {}
        self.score_table = {'a': 1, 'c': 3, 'b': 3, 'e': 1, 'd': 2, 'g': 2,
                            'f': 4, 'i': 1, 'h': 4, 'k': 5, 'j': 8, 'm': 3,
                            'l': 1, 'o': 1, 'n': 1, 'p': 3, 's': 1, 'q': 10,
                            'r': 1, 'u': 1, 't': 1, 'w': 4, 'v': 4, 'y': 4,
                            'x': 8, 'z': 10}

    def get_user_input(self):
        """returns words"""
        # user letters input in lowercase
        self.letters = raw_input('Enter your letters: ')
        while not self.letters.isalpha():
            print 'You must enter alphabetic character(s).'
            self.letters = raw_input('Enter your letters: ')

        # obligatory letters
        self.obligatory = raw_input('Enter letters which must be used or '
                                    'skip by pressing Enter: '
                                    )
        while not self.obligatory.isalpha() and self.obligatory != '':
            print 'You must enter alphabetic character(s).'
            self.obligatory = raw_input('Enter letters which must be used or '
                                        'skip by pressing Enter: '
                                        )
        while self.obligatory_check(self.letters, self.obligatory):
            print 'Letters you entered are not from your letter you gave.'
            self.obligatory = raw_input('Enter letters which must be used or '
                                        'skip by pressing Enter: '
                                        )

        # defines if words are to be ordered by the score or the length
        score = raw_input('Do you want to get words ordered by score (1) or '
                          'length (2)? ')
        while score not in ['1', '2']:
            print "Wrong input. Choose either '1' if you wish to get words " \
                  "ordered by score or '2' if you wish words ordered by " \
                  "length "
            score = raw_input('Do you want to get words ordered by score (1) '
                              'or length (2)? ')
        if score == '1':
            self.score = True
        elif score == '2':
            self.score = False
    # TODO mozna zkusit s return a do self.score dat tuhle metodu

    def obligatory_check(self, letters, obligatory):
        """returns True if obligatory letters are not comprised from given
        letters """
        letters_temp = list(letters)[:]
        error_message = "Letters must contain obligatory letters!"
        fail = False
        for char in obligatory:
            if char in letters_temp:
                letters_temp.remove(char)
            else:
                print error_message
                fail = True
        return fail

    def load_words(self):
        """read the file with all the possible english words
        returns list of all possible words"""
        with open('../docs/sowpods.txt', 'r') as word_file:
            words_from_file = word_file.read().lower()
        word_list = words_from_file.split('\n')  # list of all possible words
        return word_list

    def find_possible_words(self):
        """returns list of all words comprised of given letters"""
        letters = list(self.letters.lower())
        for word in self.load_words():
            rack = letters[:]
            for i in range(len(word)):
                if word[i] in rack:
                    rack.remove(word[i])
                    if i == len(word) - 1:
                        self.words.append(word)
                else:
                    break
        return self.words

    def obligatory_words(self):
        """returns list of words containing all of the obligatory letters
        only """
        obligatory = list(self.obligatory)
        words = self.find_possible_words()
        words_tmp = words[:]  # copy word list to edit
        filtered_words = []
        for word in words_tmp:
            word_index = words.index(word)
            index = []
            for char in obligatory:
                if char in word and word.find(char) not in index:
                    index.append(word.find(char))
                    word = word.replace(char, ' ', 1)
                if len(index) == len(obligatory):
                    filtered_words.append(words[word_index])
        self.words = filtered_words
        return self.words

    def assign_score(self):
        """assign scores to words if score=True, if not assign lengths
        word_score: dict"""
        if not self.obligatory == '':
            words = self.obligatory_words()
        else:
            words = self.find_possible_words()
        if self.score:
            for item in words:
                score = 0
                for i in item:
                    score += self.score_table.get(i)
                self.word_scores[item] = score
        else:
            for item in self.words:
                self.word_scores[item] = len(item)
        return self.word_scores

    def output(self, word_scores):
        """prints words sorted by their ascending score/length"""
        for key in sorted(word_scores, key=word_scores.get, reverse=False):
            print "%s: %i" % (key, word_scores[key])
        if self.score:
            print "Words are sorted by their scrabble score."
        else:
            print "Words are sorted by their length."

    def run(self):
        print "Welcome! This script helps you find best words you can create " \
              "from your letters in scrabble or scrabble-like game.\n"
        self.get_user_input()
        self.output(self.assign_score())


if __name__ == '__main__':
    Scrabble().run()
