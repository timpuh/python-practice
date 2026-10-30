try:
    country = input("enter the country: ")
    population = int(input("enter the population: "))
    area = float(input("enter the area in km2: "))

    density = population/area

    print(f"country: {country}")
    print(f"population: {population}")
    print(f"area: {area} km2")
    print(f"density: {round(density, 2)} people per km2")
except ValueError:
    print("⚠️please enter a number")
except ZeroDivisionError:
    print("⚠️area cannot be zero")