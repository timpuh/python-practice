# input 3 floats calculate their average apply ++ -- += -= *= /= to each and print the results

try:
    a = float(input("enter the first number: "))
    b = float(input("enter the second number: "))
    c = float(input("enter the third number: "))
    d = 2  # take any,but i chose 2 in += -= *= /=

    # arithmetic operations with all three numbers + - * /
    print(f"a + b + c = {round(a+b+c, 2)}")
    print(f"a - b - c = {round(a-b-c, 2)}")
    print(f"a * b * c = {round(a*b*c, 2)}")
    print(f"a / b / c = {round(a/b/c, 2)}")

    # average 
    average = (a+b+c)/3
    print(f"average: {round(average, 2)}")

    # operators wirh first number ++ -- += -= *= /=
    n = a # here n stores a to save the original number
    n += 1 # increment var(variable) +1
    print(f"{a} increment: {round(n, 2)}")
    n = a
    n -= 1 # decrement var -1
    print(f"{a} decrement: {round(n, 2)}")
    n = a
    n += d # addition assignment("+" + "=") +=
    print(f"{a} += {d}: {round(n, 2)}")
    n = a
    n -= d # subtraction assignment -=
    print(f"{a} -= {d}: {round(n, 2)}")
    n = a
    n *= d # multiplication assignment *=
    print(f"{a} *= {d}: {round(n, 2)}")
    n = a
    n /= d # division assignment /=
    print(f"{a} /= {d}: {round(n, 2)}")

    # the second number
    n = b
    n += 1
    print(f"{b} increment: {round(n, 2)}")
    n = b
    n -= 1
    print(f"{b} decrement: {round(n, 2)}")
    n = b
    n += d
    print(f"{b} += {d}: {round(n, 2)}")
    n = b
    n -= d
    print(f"{b} -= {d}: {round(n, 2)}")
    n = b
    n *= d
    print(f"{b} *= {d}: {round(n, 2)}")
    n = b
    n /= d
    print(f"{b} /= {d}: {round(n, 2)}")

    # the third number
    n = c
    n += 1
    print(f"{c} increment: {round(n, 2)}")
    n = c
    n -= 1
    print(f"{c} decrement: {round(n, 2)}")
    n = c
    n += d
    print(f"{c} += {d}: {round(n, 2)}")
    n = c
    n -= d
    print(f"{c} -= {d}: {round(n, 2)}")
    n = c
    n *= d
    print(f"{c} *= {d}: {round(n, 2)}")
    n = c
    n /= d
    print(f"{c} /= {d}: {round(n, 2)}")    
except ValueError:
    print("⚠️  please enter a number (use a dot, like 2.5)")
except ZeroDivisionError:
    print("⚠️  division by zero is not allowed")