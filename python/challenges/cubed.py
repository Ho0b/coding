def cubed(a, b, c):
    volume = a * b * c

    surfaceArea = (2 * ((a * b)  + (a * c) + (b * c)))

    return print("the volume is: ", volume), print("the surface area is: ", surfaceArea)


def main():
    a = int(input("first value: "))
    b = int(input("first value: "))
    c = int(input("first value: "))

    cubed(a, b, c)


main()