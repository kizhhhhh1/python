a=int(input("enter the number1:"))
sum=0
temp=a
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp=temp//10
    if sum==a:
        print("amstrong number")
    else:
        print("not an amstrong number")
