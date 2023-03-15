def character_locator(string, letter):
    indeces = []
    index = string.find(letter)
    while index != -1:
        indeces.append(index)
        index = string.find(letter, index + 1)
    return indeces
print(character_locator("this is javascript", 'i'))
