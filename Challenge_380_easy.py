# Challenge #380 [Easy] Smooshed Morse Code 1
# https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/

from itertools import product  # import used for bonus challenge 5

# Basic answer
morse_alpha = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.--" \
              " --.."
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

morse_split = morse_alpha.split()
words_file = open("Challenge_380_word_list.txt", "r")
words_array = words_file.read().splitlines()


def smorse(word):
    morse_encode = ''

    for letter_from_word in word:
        index = alpha.index(letter_from_word.upper())
        morse_encode += morse_split[index]
    return morse_encode


words_array_encoded = []
for word in words_array:
    words_array_encoded.append(smorse(word))

# Optional bonus challenges
# 1 - Find the only sequence that's the code for 13 different words.
def challenge_1 ():

    morse_code = {}
    # for morse in words_array_encoded:
    for morse in words_array_encoded:
        if morse in morse_code.keys():
            morse_code[morse] = morse_code[morse] + 1
        else:
            morse_code[morse] = 1


    for key in morse_code.keys():
        if morse_code[key] == 13:
            print(key)
            print(morse_code[key])


# 2 - Find the only word that has 15 dashes in a row.
def challenge_2 ():

    dashes = '---------------'

    # I know this is not the most efficient way, just wanted to test a way in less lines as possible -
    # maybe use collections package
    for encoded_word in words_array_encoded:
        if dashes in encoded_word:
            print(words_array[words_array_encoded.index(encoded_word)])
    # found word 'bottommost'


# 3 - Word 'ounterdemonstrations' is one of two 21-letter words that's perfectly balanced. Find the other one.


def challenge_3 ():
    for index, word in enumerate(words_array):
        if len(word) == 21:
            encoded_word = words_array_encoded[index]
            dots = encoded_word.count('.')
            dashes = encoded_word.count('-')
            if dots == dashes:
                print(word)
                print(words_array_encoded[index])

# found word 'overcommercialization'

# 4 - Find the only 13-letter word that encodes to a palindrome.
def challenge_4 ():
    for index, word in enumerate(words_array):
        if len(word) == 13:
            encoded_word = words_array_encoded[index]
            if encoded_word == encoded_word[::-1]:
                print(word)
                print(encoded_word)
                print(encoded_word[::-1])

# found word 'intransigence'


# 5 - Morse '--.---.---.--' is one of five 13-character sequences that does not appear in the encoding of any word.
# Find the other four.
### somethins is odd about this one. I dont think I understand it correctly

def challenge_5 ():
    chars = ['.', '-']
    combinations = [''.join(x) for x in product(chars, repeat=13)]

    words_encoded_13 = []
    for encoded in words_array_encoded:
        if len(encoded) == 13:
            words_encoded_13.append(encoded)

    print(len(words_encoded_13))
    print(len(combinations))
    print(len(set(combinations) - set(words_array_encoded)))
    print()
    not_found = []
    if '--.---.---.--' not in words_array_encoded:
        not_found.append('--.---.---.--')

    for comb in combinations:
        if comb not in words_array_encoded:
            print("Not found: {}".format(comb))
            not_found.append(comb)

    print(len(not_found))
    print(not_found)


# challenge_1()
# challenge_2()
# challenge_3()
# challenge_4()
challenge_5()