def coins(q, d, n, p):
    totalQuarters = q * .25
    totalDimes = d * .10
    totalNickles = n * .05
    totalPennies = p * .01

    totalDollarAmount = totalQuarters + totalDimes + totalNickles + totalPennies
    totalCoins = q + d + n + p

    return totalDollarAmount, totalCoins

def main():
    q = int(input("How many quarters: "))
    d = int(input("How many dimes: "))
    n = int(input("How many nickles: "))
    p = int(input("How many pennies: "))

    print("total amount in dollars plus the amount of coins is",coins(q, d, n, p))


main()