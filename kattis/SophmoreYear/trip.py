from decimal import Decimal, ROUND_HALF_UP

while True:
    students = int(input())
    
    if students == 0:
        quit()
    
    expenses = [None for x in range(students)]
    
    for i in range(students):
        expenses[i] = Decimal(input())
    
    expenses.sort(key=lambda x:x, reverse=True)
    sumExpenses = sum(expenses)
    
    mu =  sumExpenses / students
    rMu = mu.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    posExcess = negExcess = 0
    
    for expense in expenses:
        if expense > rMu:
            posExcess += expense - rMu
        else:
            negExcess += rMu - expense
    print("$"+'{0:.2f}'.format(min(posExcess, negExcess)))