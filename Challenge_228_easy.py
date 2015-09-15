def alphabetic_order (word):
    if word == "".join(sorted(word)):
        print word + " IN ORDER"
    elif "".join(sorted(word)) == word[::-1]:
        print word + " REVERSE ORDER"
    else:
        print word + " NOT IN ORDER"
    return 0



alphabetic_order('billowy')
alphabetic_order('biopsy')
alphabetic_order('chinos')
alphabetic_order('defaced')
alphabetic_order('chintz')
alphabetic_order('sponged')
alphabetic_order('bijoux')
alphabetic_order('abhors')
alphabetic_order('fiddle')
alphabetic_order('begins')
alphabetic_order('chimps')
alphabetic_order('wronged')
