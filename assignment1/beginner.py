word = input("Enter a word: ")
vowels = ['a', 'e', 'i', 'o', 'u']
brief = ''.join([letter for letter in word if letter.lower() not in vowels])
print(f"Brief version: {brief}")
