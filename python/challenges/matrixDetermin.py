from random import *

aList = [[],[]]
deter = 0

for i in range(len(aList)):
    for j in range(len(aList)):
        aList[j].append(randint(0,9))

deter = (aList[0][0] * aList[1][1]) - (aList[0][1] * aList[1][0])
absolute = abs(deter)

print(aList[0][0], aList[0][1], "\n", aList[1][0], aList[1][1])
print("the determaint is: \n" , absolute)


