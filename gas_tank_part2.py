fuel_type = input()
fuel_loaded = float(input())
club_card = input()
final_price = 0

price_gasoline = 2.22
price_diesel = 2.33
price_gas = 0.93

if fuel_type == "Gasoline":
    final_price = fuel_loaded * price_gasoline
    if club_card == "Yes":
        final_price = fuel_loaded * (price_gasoline - 0.18)
    if 20<= fuel_loaded <= 25:
        final_price *= 0.92
    if fuel_loaded > 25:
        final_price *= 0.90
elif fuel_type == "Diesel":
    final_price = fuel_loaded * price_diesel
    if club_card == "Yes":
        final_price = fuel_loaded * (price_diesel - 0.12)
    if 20<= fuel_loaded <= 25:
        final_price *= 0.92
    if fuel_loaded > 25:
        final_price *= 0.90
elif fuel_type == "Gas":
    final_price = fuel_loaded * price_gas
    if club_card == "Yes":
        final_price = fuel_loaded * (price_gas - 0.08)
    if 20<= fuel_loaded <= 25:
        final_price *= 0.92
    if fuel_loaded > 25:
        final_price *= 0.90

print(f"{final_price:.2f} lv.")