from itertools import permutations

with open('../docs/sowpods.txt', 'r') as word_file:
    word_file = word_file.read().lower()

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10
          }

word_list = word_file.split('\n')  # list of all possible words
rack = raw_input('Type your letters: ').lower()  # user letters in lowercase

# # my solution (super slow)
# # find all words combinations comprising of user letters
# combinations = []
# for n in range(len(rack) + 1):
#     for p in permutations(rack, n):
#         if p is not ():
#             combinations.append(''.join(p))
# combinations = set(combinations)  # remove duplicates
# # list only viable words from reference word_list
# words = []
# for word in combinations:
#     if word in word_list:
#         words.append(word)

# different solution (fast)
rack = list(rack)
words = []
for word in word_list:
    letters = rack[:]
    for i in range(len(word)):
        if word[i] in letters:
            letters.remove(word[i])
            if i == len(word) - 1:
                words.append(word)
        else:
            break

# common part of solutions
# assign scores to words
word_dict = {}
for item in words:
    word_dict[item] = len(item)

# print words sorted by their score
for key in sorted(word_dict, key=word_dict.get, reverse=True):
    print "%s: %i" % (key, word_dict[key])
# print len(word_dict)

