def DateRead(userInpt):
    month = userInpt[0:1]
    day = userInpt[3:5]
    year = userInpt[-4:]

    monthList = [
        "January",
        "Feburary",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
                 ]

    
    calenderFormat = f"{monthList[int(month)]} {day}, {year}"
    return calenderFormat

def main():
    userInput = input("Please enter a calender date: \n(ex: mm/dd/yyyy) \n")
    print(DateRead(userInput))
    

main()