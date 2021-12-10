T=int(input())
for i in range(T):
    a=int(input())
    b=0
    c=0
    for j in range(len(str(a))):
        b=a%10
        a=a//10
        c=c+b
    print(c)