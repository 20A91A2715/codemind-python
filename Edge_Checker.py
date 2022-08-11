a,b=map(int,input().split())
if (a-1)==b or (a+1)==b:
    print("Yes")
elif (a-9)==b or (a+9)==b:
    print("Yes")
else:
    print("No")