x,y=list(map(int,input().split()))
a=[]
b=[]
aa=[]
bb=[]
for i in range(x+y):
    z=input()
    if i<x:
        a.append(z)
    else:
        b.append(z)
for g in range(len(b)):
    if b[g] in a:
        aa=[]
        for k in range(len(a)):
            if a[k]==b[g]:
                aa.append(k+1)
        bb.append(aa)
    else:
        bb.append([-1])
for f in range(len(bb)):
    print(*bb[f])
