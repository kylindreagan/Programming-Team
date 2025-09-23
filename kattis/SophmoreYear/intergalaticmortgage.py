while True:
    amount, monthlypayment, years, rate = map(float, input().split())
    months = years * 12
    rate /= 1200

    if amount == monthlypayment == years == rate  == 0:
        break
    
    if rate == 0:
        # Special case: no interest rate means we just divide the amount evenly over months
        monthlypayment_needed = amount / months
    else:
        # Standard formula for the present value of an annuity
        monthlypayment_needed = (amount * rate) / (1 - (1 + rate) ** -months)
    
    if monthlypayment < monthlypayment_needed:
        print("NO")
    else:
        print("YES")