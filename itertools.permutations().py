from itertools import permutations
c=[]
a,b=input().split()
for i in range(len(a)):
    c.append(a[i])
c.sort()
d=list(permutations(c,int(b)))
for k in range (len(d)):
    print("".join(d[k]))
