def compare_base62(s:str, n:int, s2:str)->int:
    for i in range(n):
        chr1, chr2 = s[i], s2[i]
        
        if chr1.isdigit():
            digit1 = int(chr1)
        elif chr1.islower():
            digit1 = ord(chr1) - 87
        else:
            digit1 = ord(chr1) - 29
        
        if chr2.isdigit():
            digit2 = int(chr2)
        elif chr2.islower():
            digit2 = ord(chr2) - 87
        else:
            digit2 = ord(chr2) - 29

        if digit2 > digit1:
            return False
        if digit1 > digit2:
            return True


for i in range(int(input())):
    strnum1 = input()
    strnum2 = input()
    
    len1 = len(strnum1)
    len2 = len(strnum2)
    firststrbigger = strnum1 > strnum2

    if len1 == len2:
        firstnumbigger = compare_base62(strnum1, len1, strnum2)
        if (firstnumbigger and firststrbigger) or (not firstnumbigger and not firststrbigger):
            print("YES")
        else:
            print("NO")

    elif (len1 < len2 and firststrbigger) or (len1 > len2 and not firststrbigger):
        print("NO")
    
    else:
        print("YES")