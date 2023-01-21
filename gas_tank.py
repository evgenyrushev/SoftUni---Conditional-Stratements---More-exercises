type_fuel = input()
liters = int(input())

if type_fuel == "Diesel":
    if liters >= 25:
        print(f"You have enough diesel.")
    elif liters < 25:
        print(f"Fill your tank with diesel!")
elif type_fuel == "Gasoline":
    if liters >= 25:
        print(f"You have enough gasoline.")
    elif liters < 25:
        print(f"Fill your tank with gasoline!")
elif type_fuel == "Gas":
    if liters >= 25:
        print(f"You have enough gas.")
    elif liters < 25:
        print(f"Fill your tank with gas!")
else:
    print("Invalid fuel!")