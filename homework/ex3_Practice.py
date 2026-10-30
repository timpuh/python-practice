name = input("enter the billionaires name: ")
age = int(input("enter age: "))
money = float(input("enter net worth in dollars: "))

per_year = money/age
per_month = per_year/12
per_day = per_year/365
per_hour = per_day/24
per_minute = per_hour/60
per_second = per_minute/60

print(f"billionaire: {name}, age: {age}")
print(f"net worth: {money} dollars")
print(f"per year: {round(per_year, 2)} dollars")
print(f"per month: {round(per_month, 2)} dollars")
print(f"per day: {round(per_day, 2)} dollars")
print(f"per hour: {round(per_hour, 2)} dollars")
print(f"per minute: {round(per_minute, 2)} dollars")
print(f"per second: {round(per_second, 2)} dollars")