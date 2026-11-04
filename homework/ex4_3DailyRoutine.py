# ask for the hour (0-23) and tell what to do at that time
# 8-16 office, 16-17 gym, 17-20 beach, plus breakfast, lunch, dinner and night sleep

try:
    hour = int(input("enter the hour (0-23): "))

    if hour < 0 or hour > 23:
        print("⚠️  hour must be from 0 to 23")
    elif hour < 7:
        print("sleep")
    elif hour < 8:
        print("breakfast")
    elif hour >= 12 and hour < 13:
        print("lunch")
    elif hour < 16:
        print("office")
    elif hour < 17:
        print("gym")
    elif hour < 20:
        print("beach")
    elif hour < 21:
        print("dinner")
    else:
        print("sleep")
except ValueError:
    print("⚠️  please enter a whole number")

# hour < 16 means all hours up to 15. 16 does not pass here it goes to the next elif. So the code always uses < not <=