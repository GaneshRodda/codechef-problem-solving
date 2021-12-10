n=int(input())
for i in range(n):
    a=int(input())
    d=0
    for j in range(len(str(a))):
        d=d*10+(a%10)
        a=a//10
    print(d)