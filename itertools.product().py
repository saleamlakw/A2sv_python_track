from itertools import product
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=list(product(a,b))
print(*a)
