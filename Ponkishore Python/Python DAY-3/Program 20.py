num = input("enter a number1:")

if len(num) % 2 == 0:
    mid = len(num) // 2
    first_half = num[:mid]
    second_half = num[mid:]
    
    first_sum = sum(int(digit) ** 2 for digit in first_half)
    second_sum = sum(int(digit) ** 2 for digit in second_half)
    
    if first_sum + second_sum == int(num):
        print(f"{num} is a tech number")
    else:
        print(f"{num} is not a tech number")
else:
    print(f"{num} is not a tech number")
