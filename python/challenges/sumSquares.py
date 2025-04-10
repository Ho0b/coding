import math as m


def sumsquares(n):

    sum = 0

    for i in range(n): 
        squared = m.pow(i, 2)
        sum += squared
    
    
    return sum


def main():
    
    userInpt = int(input("Please input how many numbers to find the sum of squares for: "))
    print(sumsquares(userInpt))

main()
