# TODO Transform to class and individual methods
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

    def __init__(self, letters, obligatory, score=True):
        self.letters = letters
        self.obligatory = obligatory
        self.score = score
        self.words = []
        self.word_scores = {}
        if self.score:
            self.score_table = {'a': 1, 'c': 3, 'b': 3, 'e': 1, 'd': 2, 'g': 2,
                                'f': 4, 'i': 1, 'h': 4, 'k': 5, 'j': 8, 'm': 3,
                                'l': 1, 'o': 1, 'n': 1, 'q': 10, 'p': 3,
                                's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 4, 'v': 4,
                                'y': 4, 'x': 8, 'z': 10
                                }


    def load_words(self):
        """read the file with all the possible english words
        returns list of all possible words"""
        with open('../docs/sowpods.txt', 'r') as word_file:
            words_from_file = word_file.read().lower()
        word_list = words_from_file.split('\n')  # list of all possible words
        return word_list


    def find_possible_words(self):
        """returns list of all words comprised of given letters"""
        letters = list(self.letters.lower())  # transform user letters to lower letter list
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
        """returns list of words containing all of the obligatory letters only"""
    # if self.obligatory != '':
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
        """assign scores to words if score=True, if not assign lengths"""
        if self.obligatory != '':
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


    def printer(self, word_scores):
        """prints words sorted by their ascending score/length"""
        for key in sorted(word_scores, key=word_scores.get, reverse=False):
            print "%s: %i" % (key, word_scores[key])
        if self.score:
            print "Words are sorted by their scrabble score."
        else:
            print "Words are sorted by their length."


    def run(self):
        self.printer(self.assign_score())


def run():
    '''returns words'''
    # user letters input
    letters = raw_input('Enter your letters: ')
    while not letters.isalpha():
        print 'You must enter alphabetic character(s).'
        letters = raw_input('Enter your letters: ')

    # obligatory letters
    obligatory = raw_input('Enter letters which must be used: ')
    while not obligatory.isalpha() and obligatory != '':
        print 'You must enter alphabetic character(s).'
        obligatory = raw_input('Enter letters which must be used: ')
    while obligatory_check(letters, obligatory):
        obligatory = raw_input('Enter letters which must be used: ')

    # defines if words are to be ordered bz the score or the length
    score = raw_input('Do you want to get words ordered by score (1) or '
                      'length (2)? ')
    while score not in ['1', '2']:
        print "Wrong input. Choose either '1' if you wish to get words ordered " \
              "by score or '2' if you wish words ordered by length "
        score = raw_input('Do you want to get words ordered by score (1) or '
                          'length (2)? ')
    if score == '1':
        score = True
    elif score == '2':
        score = False

    Scrabble(letters, obligatory, score).run()


def obligatory_check(letters, obligatory):
    """returns error if obligatory letters are not from letters"""
    letters_temp = letters[:]
    error_message = "Letters must contain obligatory letters!"
    fail = False
    for char in obligatory:
        if char in letters_temp:
            letters_temp.remove(char)
        else:
            print error_message
            fail = True
    return fail


run()