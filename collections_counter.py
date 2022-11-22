from collections import Counter
x=int(input())
y=list(map(int,input().split()))
k=Counter(y)
z=int(input())
price=0
for i in range(z):
    a,b=list(map(int,input().split()))
    if a in k.keys():
        if k[a]>0:
            price+=b
            k[a]=k[a]-1
print(price)

