
phrase = input("Please enter your full name: \n")

stringSplit = phrase.split(" ")

for i in range(len(stringSplit)):
    f = stringSplit[i]
    m = stringSplit[i+1]
    l = stringSplit[i+2]

print(f, ".", m, ".", l, ".")


