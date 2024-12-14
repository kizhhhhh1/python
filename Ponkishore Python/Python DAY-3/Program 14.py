num = int(input("enter a number1:"))
digit_sum = sum(int(digit) for digit in str(num))

if num % digit_sum == 0:
    print(f"{num} is a harshad number")
else:
    print(f"{num} is not a harshad number")
