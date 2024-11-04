import random as r
import math

numberOfItterations = r.randint(5,20)
print(numberOfItterations)
listOfNumbers = [numberOfItterations]
negativeNums = list()
sum = 0
sumOfNegativeNums = 0

for i in range(numberOfItterations):
    value = r.randint(-10,10)
    listOfNumbers.insert(i, value)
    sum += listOfNumbers[i]
    print(listOfNumbers[i])
    print("value of i at:", i, " is ", listOfNumbers[i])

    if (value < 0):
        negativeNums.append(abs(value))
        sumOfNegativeNums += abs(value)

count = len(listOfNumbers)
print(sum)
sum /= count

print("the number of items in the array: ", count-1)
print("sum of the array is: ", sum)
print("the numbers of negative values: ", len(negativeNums))
print("sum of negative values ", sumOfNegativeNums)
