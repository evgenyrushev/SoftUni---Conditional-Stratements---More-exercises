number_kilometers = int(input())
time_of_day = input()
price = 0

if 0 <= number_kilometers < 20:
    if time_of_day == "day":
        price = 0.7 + 0.79 * number_kilometers
    if time_of_day == "night":
        price = 0.7 + 0.90 * number_kilometers
elif 20 <= number_kilometers < 100:
    price = 0.09 * number_kilometers
elif number_kilometers >= 100:
    price = 0.06 * number_kilometers

print(f"{price:.2f}")


