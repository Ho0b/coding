phrase = "The quick brown fox jumps over the lazy dog"

stringList = phrase.split(' ')

charList = []

for ch in phrase:
    if ch == ' ':
        pass
    else:
        charList += ch

wordLength = len(stringList)
letterLength = len(charList)
print(wordLength, " Words")
print(letterLength, " Letters")
print("The average number of characters is: ", round((letterLength / wordLength), 2), " letters")