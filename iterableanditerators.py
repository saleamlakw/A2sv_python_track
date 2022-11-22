from itertools import permutations,groupby
x=int(input())
y=input().split()
z=int(input())
k=list(permutations(y,z))
a=0
all=len(k)
for j in range(len(k)):
    if "a" in k[j]:
        a+=1
print(float(a/all))
