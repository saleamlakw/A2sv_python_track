from itertools import groupby
y=input()
x=[]
a=()
z=[]
for j in range(len(y)):
    x.append(int(y[j]))
key_func = lambda h: h
i=0
for key, group in groupby(x, key_func):
    a = (len(list(group)),)
    b = key
    c=(*a,b)
    z.append(c)
print(*z)


