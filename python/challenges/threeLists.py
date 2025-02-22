from random import *

def Travel(n):
    speedList = []
    timeList = []
    distanceList = []

    for i in range(n):
        speedList.append(randint(50,70))
        timeList.append(randint(1,10))

    for j in range(n):
        distanceList.append(speedList[j] * timeList[j])



    return n 

    

def main():

    userInput = int(input("Please enter a number of travels: (integer) \n"))
    Travel(userInput)

main()