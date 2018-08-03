print("think of any number between 0 and 100")
print("Is your secret number 50?")
ans=input("enter the option")
low=0
high=100
mid=(low+high)//2
while(ans!='c'):
    if(ans=='l'):
        low=mid
        mid=(mid+high)//2
    elif(ans=='h'):
        high=mid
        mid=(mid+low)//2
    else:
        print("invalid output")
    print("is your secret number is ", mid)
    ans=input("enter the option")
if(ans=='c'):
    print(mid)

