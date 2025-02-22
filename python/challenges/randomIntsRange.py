from random import *

def randInter(n):
    posNum = 0
    negNum = 0
    zeroNum = 0
    numList = [n]

    for i in range(n):
        numList.append(randint(-99,99))

    for j in numList:
        if j > 0:
            posNum += 1
        elif j < 0:
            negNum += 1
        else:
            zeroNum += 1

    return posNum, negNum, zeroNum, numList


userInput = True

while userInput:
    n = int(input("Please specify the amount of numbers to generate from -99 to 99: (limit: 100 numbers) \n"))
    if n < 100:
        posNum, negNum, zeroNum, numList = randInter(n)
        userInput = False
    else:
        print("this value is higher than 100: try again...")

print(numList)
print(f"there is {posNum} positive numbers \n", f"there is {negNum} negative numbers \n", f"there is {zeroNum} zeros \n")