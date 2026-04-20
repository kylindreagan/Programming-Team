#https://open.kattis.com/problems/astrologicalsign
def starSign(month: str, day: int) -> str:
    signs = [
        (1, 21, "Aquarius"),
        (2, 20, "Pisces"),
        (3, 21, "Aries"),
        (4, 21, "Taurus"),
        (5, 21, "Gemini"),
        (6, 22, "Cancer"),
        (7, 23, "Leo"),
        (8, 23, "Virgo"),
        (9, 22, "Libra"),
        (10, 23, "Scorpio"),
        (11, 23, "Sagittarius"),
        (12, 22, "Capricorn")
    ]
    for m, d, sign in reversed(signs):
        if (month, day) >= (m, d):
            return sign
    return "Capricorn"

sToN = {"Jan":1, "Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9, "Oct":10, "Nov":11, "Dec":12}

for i in range(int(input())):
    day, month = input().split()
    mInt = sToN[month]
    print(starSign(mInt, int(day)))