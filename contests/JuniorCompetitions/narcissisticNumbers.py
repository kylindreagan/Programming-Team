def precompute(n:int):
    exp_dict = {i: [x**i for x in range(10)] for i in range(1,n)}
    return exp_dict

exp_dict = precompute(17)
for i in range(int(input())):
    num = input()
    length = len(num)
    print("Case #"+ str(i+1) +":", end=" ")
    curr_dict = exp_dict[length]
    child_num = sum(curr_dict[int(x)] for x in num)
    print("YES" if child_num == int(num) else "NO")
