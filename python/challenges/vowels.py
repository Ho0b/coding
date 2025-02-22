phrase = "Department of computer science at Widener University"
phraseLowered = phrase.lower()

vowelsCount = 0
consonantCount = 0

for i in phraseLowered:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowelsCount += 1
    else:
        consonantCount += 1

print("there are", vowelsCount, "Vowels", " and", consonantCount, "Consonants")