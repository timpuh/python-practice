# ask for a number of days (28, 29, 30 or 31) and print the months that have that many days

try:
    days = int(input("enter the number of days in a month (28, 29, 30 or 31): "))

    match days:
        case 28 | 29:
            print("february (28 days, 29 in a leap year)")
        case 30:
            print("april, june, september, november")
        case 31:
            print("january, march, may, july, august, october, december")
        case _:
            print("⚠️  no month has that many days")
except ValueError:
    print("⚠️  please enter a whole number")
