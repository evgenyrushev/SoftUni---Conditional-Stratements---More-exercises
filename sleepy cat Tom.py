import math
number_vacation_days = int(input())

minutes_for_play = 30000
workdays_minutes_for_play = 63
weekends_mintues_for_play = 127
number_workdays = 365 - number_vacation_days

total_minutes = workdays_minutes_for_play * number_workdays + weekends_mintues_for_play * number_vacation_days

if total_minutes > minutes_for_play:
    print("Tom will run away")
    a = total_minutes - minutes_for_play
    h = a // 60
    h = math.floor(h)
    m = a % 60
    print(f"{h} hours and {m} minutes more for play")
else:
    print("Tom sleeps well")
    b = minutes_for_play - total_minutes
    ho = b // 60
    ho = math.floor(ho)
    mi = b % 60
    print(f"{ho} hours and {mi} minutes less for play")



