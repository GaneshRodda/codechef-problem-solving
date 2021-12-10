T=int(input())
for i in range(T):
    p=int(input())
    p=str(p)
    k=0
    for i in p:
        if i=="4":
            k+=1
    print(k)