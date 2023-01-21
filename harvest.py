from math import ceil, floor
sq_meters = int(input())
kg_grapes_per_sqm = float(input())
required_liters_wine = int(input())
number_workers = int(input())

kilo_grapes = sq_meters * kg_grapes_per_sqm
wine_produced = 0.4 * kilo_grapes / 2.5

if wine_produced < required_liters_wine:
    print(f"It will be a tough winter! More {floor(required_liters_wine - wine_produced)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(wine_produced)} liters.")
    print(f"{ceil(wine_produced - required_liters_wine)} liters left ->"
          f" {ceil((wine_produced - required_liters_wine) / number_workers)} liters per person.")
