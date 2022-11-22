from itertools import combinations
c=[]
a,b=input().split()
for i in range(len(a)):
    c.append(a[i])
c.sort()
for j in range(1,int(b)+1):
    d=list(combinations(c,j))
    for k in range (len(d)):
        print("".join(d[k]))
