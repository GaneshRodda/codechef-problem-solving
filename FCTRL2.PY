n=int(input())
for i in range(n):
    a=int(input())
    k=1
    for j in range(a):
        k=k*a
        a-=1
    print(k)