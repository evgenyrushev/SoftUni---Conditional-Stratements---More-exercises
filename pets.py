from math import floor, ceil
days_absent = int(input())
food_left_in_kg = int(input())
dog_eats_per_day = float(input())
cat_eats_per_day = float(input())
turtle_eats_per_day = float(input()) / 1000

food_eaten = dog_eats_per_day * days_absent + cat_eats_per_day * days_absent + turtle_eats_per_day * days_absent

if food_eaten <= food_left_in_kg:
    print(f"{floor(food_left_in_kg - food_eaten)} kilos of food left.")
else:
    print(f"{ceil(food_eaten - food_left_in_kg)} more kilos of food are needed.")