# write a program that takes speed distance and a factor (0.2-sleep, 0.5-read, 0.9-talk, 1-silence) 
# to calculate and output actual and relative travel times in hours and minutes

try:
    speed = float(input("enter the speed in km/h: "))
    distance = float(input("enter the distance in km: "))
    print("relativity coefficient: 0.2 - sleeping, 0.5 - reading or video, 0.9 - talking, 1 - silence")
    coefficient = float(input("enter the coefficient: "))

    real_hours = distance/speed
    relative_hours = real_hours*coefficient

    real_minutes = real_hours*60
    relative_minutes = relative_hours*60

    print(f"real time: {round(real_hours, 2)} h = {round(real_minutes, 1)} min")
    print(f"relative time: {round(relative_hours, 2)} h = {round(relative_minutes, 1)} min")
except ValueError:
    print("⚠️  please enter a number")
except ZeroDivisionError:
    print("⚠️  speed cannot be zero")

# actually the task is a bit confusing just because of how it's written 🗿