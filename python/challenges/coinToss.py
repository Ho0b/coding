from random import Random, randint
from secrets import randbelow


def coinTossing(n):
    totalOccurances = 0

    heads = 0
    tails = 0

    for i in range(n):
        if (Random.randint(0, 1)) == 0:
            print("Head")
            heads += 1
            totalOccurances += 1
        else:
            print("Tails")
            tails += 1
            totalOccurances += 1

    return print("heads: ", heads), print("tails: ", tails)

def main():

    n = int(input("how many times to flip a coin: "))

    coinTossing(n)


main()