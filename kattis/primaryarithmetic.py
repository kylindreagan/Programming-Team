while True:
    num1, num2 = input().split()
    if num1 == num2 == "0":
        break
    l1, l2 = len(num1), len(num2)
    carries = 0
    is_carry = False
    num1, num2 = num1[::-1], num2[::-1]
    for i in range(min(l1,l2)):
        if int(num1[i])+int(num2[i])+is_carry >= 10:
            carries += 1
            is_carry = True
        else:
            is_carry = False
    if l1>l2:
        for i in range(l1-l2):
            if num1[i+l2] == "9" and is_carry:
                carries += 1
            else:
                break
    elif l1<l2:
        for i in range(l2-l1):
            if num2[i+l1] == "9" and is_carry:
                carries += 1
            else:
                break
    if carries == 0:
        print("No carry operation.")
    elif carries == 1:
        print("1 carry operation.")
    else:
        print(f"{carries} carry operations.")