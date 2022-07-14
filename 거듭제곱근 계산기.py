x= input()
z=int(x)
y=0
for i in range (0, 20) :
    a=10**i
    b=1/a
    c=1
    d=b
    while (y+d)**2<=z:
        c+=1
        d=c*b
    c=c-1
    d=c*b
    y=y+d





    
print(y)


import math
print(math.sqrt(z))

# 루트7이 값이 다름