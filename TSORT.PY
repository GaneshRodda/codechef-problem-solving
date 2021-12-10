g=[]
e=int(input())
for i in range(e):
    a=int(input())
    g.append(a)
for k in range(e):
    if g[k]>g[k+1]:
        g[k],g[k+1]=g[k+1],g[k]
for j in g:
    print(j)