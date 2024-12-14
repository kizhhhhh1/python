a=int(input("enter a number1:"))
sum=0
for i in range(1,a):
    if(a%i==0):
        sum=sum+i
    if(sum==a):
        print("%d is a perfect number" %a)
    else:
        print("%d is not a perfect number" %a)
