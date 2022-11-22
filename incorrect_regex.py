import re 
x=int(input())
for i in range(x):
    y=input()
    try:
        re.compile(y)
        print(True)
    except:
        print(False)
