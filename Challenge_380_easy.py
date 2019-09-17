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
# 1

words_file = open("Challenge_380_word_list.txt", "r")
words_array = words_file.read().splitlines()

words_array_encoded = []

for word in words_array:
    words_array_encoded.append(smorse(word))

morse_code = {}
# for morse in words_array_encoded:
for morse in words_array_encoded:
    # if morse == '-...-....-.--.':
        # print(morse)
    if morse in morse_code.keys():
        morse_code[morse] = morse_code[morse] + 1
    else:
        morse_code[morse] = 1


for key in morse_code.keys():
    if morse_code[key] == 13:
        print(key)
        print(morse_code[key])

# 2

