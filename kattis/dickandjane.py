while True:
    try:
        s,p,y,j = map(int, input().split())
        """
        s- Age spot (S) was when puff was born
        p- Age puff (P) was when yertle was born
        y- Age spot was when yertle (Y) was born 
        j- Jane's age
        """

        age_diff = j + 12 - (y + p) #Total age of pets = janes age + 12
        remainder = age_diff % 3
        quotient = age_diff // 3
        if remainder == 0:
            S = y + quotient
            P = p + quotient
            Y = quotient
        elif remainder == 1:
            S = y + quotient + 1
            P = p + quotient
            Y = quotient
            if y - p > s and S - P > s:
                S -= 1
                P += 1
        elif remainder == 2:
            S = y + quotient + 1
            P = p + quotient + 1
            Y = quotient
        else:
            raise ValueError
        print(S,P,Y)
    except EOFError:
        quit()