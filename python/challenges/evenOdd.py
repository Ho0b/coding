import keyboard

running = True
userInput = 0

def isEven(userInput):
    if userInput % 2 == 0:
        print( userInput, " is Even")
    else:
        print( userInput, " is Odd")

def onStop():
    print("Stopped")
    running = False

while running is not False:
    print("Please input a number to see if it is even: ")
    userInput = int(input())
    isEven(userInput)

    print("run again? y/n")
    confirmation = input()

    if confirmation == "y":
        print("Continuing...")
    else:
        onStop()
        break
