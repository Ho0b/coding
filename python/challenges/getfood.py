from hmac import new
from types import new_class


def phonenumber(userin = str):
    capit = userin.upper()

    newString = []

    for ch in capit:
        newString.append(ch)
    
    print(newString)
    
    for i in range(len(newString)):
        if newString[i] == 'A' or newString[i] == 'B' or newString[i] == 'C':
            newString[i] = "2"
        if newString[i] == 'D' or newString[i] == 'E' or newString[i] == 'F':
            newString[i] = "3"
        if newString[i] == 'G' or newString[i] == 'H' or newString[i] == 'I':
            newString[i] = "4"
        if newString[i] == 'J' or newString[i] == 'K' or newString[i] == 'L':
            newString[i] = "5"
        if newString[i] == 'G' or newString[i] == 'N' or newString[i] == 'O':
            newString[i] = "6"
        if newString[i] == 'P' or newString[i] == 'Q' or newString[i] == 'R' or newString[i] == 'S':
            newString[i] = "7"
        if newString[i] == 'T' or newString[i] == 'U' or newString[i] == 'V':
            newString[i] = "8"
        if newString[i] == 'W' or newString[i] == 'X' or newString[i] == 'Y' or newString[i] == 'Z' :
            newString[i] = "9"

    combined = ''.join(newString)

    return combined

inpt = input("Please enter a 10 character phone number: ex. XXX-XXX-XXXX \n")
print(phonenumber(inpt))