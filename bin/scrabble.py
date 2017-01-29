# TODO Transform to class and individual methods
def scrabble(letters, obligatory, score=True):
    """
    List all possible words and theirs score (if score=True), comprised
    of entered letters as a string.
    Optional: obligatory letters - letters which must be used.

    types
    letters: str
    obligatory: str
    score: boolean
    """
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
              "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
              "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
              "x": 8, "z": 10}
    # read the file with all the possible english words
    with open('../docs/sowpods.txt', 'r') as word_file:
        word_file = word_file.read().lower()

    word_list = word_file.split('\n')  # list of all possible words

    letters = list(letters.lower())
    words = []
    for word in word_list:
        rack = letters[:]
        for i in range(len(word)):
            if word[i] in rack:
                rack.remove(word[i])
                if i == len(word) - 1:
                    words.append(word)
            else:
                break

    # error if obligatory letters are not from letters
    letters_temp = letters[:]
    for char in obligatory:
        if char in letters_temp:
            letters_temp.remove(char)
        else:
            print "Letters must contain obligatory letters!"

    # list words containing all of obligatory letters only
    if obligatory != '':
        obligatory = list(obligatory)
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
        words = filtered_words

    # assign scores to words if score=True, if not assign lengths
    word_dict = {}
    if score:
        for item in words:
            score = 0
            for i in item:
                score += scores.get(i)
            word_dict[item] = score
    else:
        for item in words:
            word_dict[item] = len(item)

    # print words sorted by their ascending score/length
    for key in sorted(word_dict, key=word_dict.get, reverse=False):
        print "%s: %i" % (key, word_dict[key])
    if score:
        print "Words are sorted by their scrabble score."
    else:
        print "Words are sorted by their length."


l = raw_input('Enter your letters: ')
o = raw_input('Enter letters which must be used: ')
s = raw_input('Do you want to get words ordered by score (1) or length (2)? ')
# if s == '1':
#     s = True
# elif s == '2':
#     s = False
scrabble(l, o, True if s == '1' else False)
