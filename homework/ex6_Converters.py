# write programs to change miles to kilometers fahrenheit to celsius and back pounds to kilorams and inches to millimeters

# miles -> kilometers
try:
    m = float(input("enter miles: "))
    print(f"{m} miles = {round(m*1.609, 3)} km")
except ValueError:
    print("⚠️  please enter a number")

# fahrenheit -> celsius
try:
    f = float(input("enter degrees fahrenheit: "))
    print(f"{f} °F = {round((f-32)/1.8, 2)} °C")
except ValueError:
    print("⚠️  please enter a number")

# celsius -> fahrenheit
try:
    c = float(input("enter degrees Celsius: "))
    print(f"{c} °C = {round(c*1.8+32, 2)} °F")
except ValueError:
    print("⚠️  please enter a number")

# pounds -> kilograms
try:
    p = float(input("enter pounds: "))
    print(f"{p} lb = {round(p/2.2046, 5)} kg")
except ValueError:
    print("⚠️  please enter a number")

# inches -> millimeters
try:
    i = float(input("enter inches: "))
    print(f"{i} in = {round(i*25.4, 2)} mm")
except ValueError:
    print("⚠️  please enter a number")
