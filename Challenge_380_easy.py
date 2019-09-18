# Challenge #380 [Easy] Smooshed Morse Code 1
# https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/

# Basic answer
morse_alpha = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.--" \
              " --.."
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

morse_split = morse_alpha.split()


def smorse(word):
    morse_encode = ''

    for letter_from_word in word:
        index = alpha.index(letter_from_word.upper())
        morse_encode += morse_split[index]
    return morse_encode


# Optional bonus challenges
# 1 - Find the only sequence that's the code for 13 different words.
print('#1')

words_file = open("Challenge_380_word_list.txt", "r")
words_array = words_file.read().splitlines()

words_array_encoded = []

for word in words_array:
    words_array_encoded.append(smorse(word))

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

print('===========================================================================')
print('===========================================================================')
print('===========================================================================\n\n')
print('#2')

# 2 - Find the only word that has 15 dashes in a row.

dashes = '---------------'

# I know this is not the most efficient way, just wanted to test a way in less lines as possible -
# maybe use collections package
for encoded_word in words_array_encoded:
    if dashes in encoded_word:
        print(words_array[words_array_encoded.index(encoded_word)])
# found word 'bottommost'

print('===========================================================================')
print('===========================================================================')
print('===========================================================================\n\n')
print('#3')

# 3 - Word 'ounterdemonstrations' is one of two 21-letter words that's perfectly balanced. Find the other one.


for index, word in enumerate(words_array):
    if len(word) == 21:
        encoded_word = words_array_encoded[index]
        dots = encoded_word.count('.')
        dashes = encoded_word.count('-')
        if dots == dashes:
            print(word)
            print(words_array_encoded[index])

# found word 'overcommercialization'


print('===========================================================================')
print('===========================================================================')
print('===========================================================================\n\n')
print('#4')

# 4 - Find the only 13-letter word that encodes to a palindrome.
for index, word in enumerate(words_array):
    if len(word) == 13:
        encoded_word = words_array_encoded[index]
        if encoded_word == encoded_word[::-1]:
            print(word)
            print(encoded_word)
            print(encoded_word[::-1])

# found word 'intransigence'

print('===========================================================================')
print('===========================================================================')
print('===========================================================================\n\n')
print('#5')

# 5 - Morse '--.---.---.--' is one of five 13-character sequences that does not appear in the encoding of any word.
# Find the other four.
