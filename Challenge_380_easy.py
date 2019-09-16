# Challenge #380 [Easy] Smooshed Morse Code 1
# https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/

# Basic answer
morse_alpha = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.--" \
              " --.."
alpha = "ABCEDFGHIJKLMNOPQRSTUVWXYZ"

morse_split = morse_alpha.split()


def smorse(word):
    morse_encode = ''

    for letter_from_word in word:
        index = alpha.index(letter_from_word.upper())
        morse_encode += morse_split[index]
    return morse_encode


# print(smorse('programmer'))

# Optional bonus challenges

# 1

words_file = open("Challenge_380_word_list.txt", "r")
words_array = words_file.read().splitlines()

words_array_encoded = []

for word in words_array:
    words_array_encoded.append(smorse(word))

#TODO find only sequence that repeat 13 times

