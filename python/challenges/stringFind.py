def find(a = str):
    phraseA = "CSCI 152"
    phraseB = "MATH 152"

    newStr = str(a.upper())

    if newStr.find(phraseA) != -1 :
        print(phraseA, " was found")
    if newStr.find(phraseB) != -1 :
        print(phraseB, " was found")
    else:
        print("could not be found...")

find(input())