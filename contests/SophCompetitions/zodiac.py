T = int(input())
for i in range(T):
    year = int(input())
    zodiac = year%12

    if(zodiac == 0):
        print(year, "is the year of the monkey")
    elif(zodiac == 1):
        print(year, "is the year of the rooster")
    elif(zodiac == 2):
        print(year, "is the year of the dog")
    elif(zodiac == 3):
        print(year, "is the year of the pig")
    elif(zodiac == 4):
        print(year, "is the year of the rat")
    elif(zodiac == 5):
        print(year, "is the year of the ox")
    elif(zodiac == 6):
        print(year, "is the year of the tiger")
    elif(zodiac == 7):
        print(year, "is the year of the rabbit")
    elif(zodiac == 8):
        print(year, "is the year of the dragon")
    elif(zodiac == 9):
        print(year, "is the year of the snake")
    elif(zodiac == 10):
        print(year, "is the year of the horse")
    elif(zodiac == 11):
        print(year, "is the year of the sheep")