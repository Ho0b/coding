inpt = input("Please enter your full name; \n")
fixedString = inpt.replace(" ", '')
reversedString = []

count = 1
for i in fixedString:
    reversedString.append(fixedString[-count])
    count += 1
    print(count)

finishedString = "$$" + ''.join(reversedString) + "$$"

print(finishedString)