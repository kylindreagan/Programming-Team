for i in range(int(input())):
    year_f, year_l = map(int, input().split())
    total_years = year_l - year_f
    running_years = 0
    if year_f == 1600:
        running_years += 1
    if year_f <= 2000 and year_l >= 2000:
        running_years += 1
    running_years += total_years % 4
    running_years -= year_l // 100 - year_f // 100
    if running_years == 1:
        print("There is 1 leap year between", year_f, "and", str(year_l) + ".")
    else:
        print("There are", running_years, "leap years between", year_f, "and", str(year_l) + ".")