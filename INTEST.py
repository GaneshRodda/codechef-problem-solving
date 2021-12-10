n,k=map(int,input().split())
c=0
for i in range(n):
    ti=int(input())
    if ti%k==0:
        c+=1
print(c)