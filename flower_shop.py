from math import floor, ceil

number_magno = int(input())
number_zumbul = int(input())
number_roses = int(input())
number_cactus = int(input())
price_for_gift = float(input())

magno_price = 3.25
zumbul_price = 4
rose_price = 3.50
cactus_price = 8

amount_ordered = number_cactus * cactus_price + \
                 number_roses * rose_price + \
                 number_magno * magno_price + \
                 number_zumbul * zumbul_price
amount_with_tax = amount_ordered * 0.95

if amount_with_tax >= price_for_gift:
    print(f"She is left with {floor(amount_with_tax - price_for_gift)} leva.")
else:
    print(f"She will have to borrow {ceil(price_for_gift - amount_with_tax)} leva.")
