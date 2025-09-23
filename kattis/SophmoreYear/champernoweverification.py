n,y=input(),"123456789";c=len(n); 
if c>9:
    print(-1) 
    quit()
if y[:c] == n:print(c)
else:print(-1)
