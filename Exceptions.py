x=int(input())
for i in range(x):
    try:
        y,z=list(map(int,input().split()))
        try:
            print(y/z)
        except Exception as e : 
            print("Error Code:",e)
    except Exception as f:
        print("Error Code:",f)
