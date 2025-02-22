mtx = [[3,0,2,5,6], [1,-2,3,-4,0],[-3,2,4,-7,7]]

for i in mtx:
    print(i)

running = True

print("Welcome to a matrix program!\n press any of the numbers to perform certain tasks")
print("(1): count, then give all positive numbers")
print("(2): count, then give all zeros")
print("(3): count, then prints total all negative numbers")
print("(4): stops this program")

while(running):
    
    userInput = input("Please type a number: ")

    if userInput == 1:
        for i in mtx:
            for j in mtx:
                posCount = 0
                if mtx[i][j] >= 0:
                    pass
                else:
                    posCount += 1
        print("the total amount of positive numbers is", posCount)
    elif userInput == 2:
        for a in mtx:
            for b in mtx:
                zerosCount = 0
                if mtx[i][j] == 0:
                    zerosCount += 1
                else:
                    pass
        print("the total amount of zeros is", zerosCount)
    elif userInput == 3:
        for c in mtx:
            for d in mtx:
                negativeCount = 0
                if mtx[i][j] <= 0:
                    negativeCount += 1
        print("the total amount of negative numbers is", negativeCount)
    elif userInput == 4:
        running = False
        break