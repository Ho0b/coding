
phrase = input("Please any of your favorite phrases: \n")

charListUpper = []
charListLower = []

for ch in phrase:
    if ch.isupper():
        charListUpper += ch
    elif ch.islower():
        charListLower += ch

print("there are ", len(charListUpper), " capital letters")
print("there are ", len(charListLower), " lower case letters")
