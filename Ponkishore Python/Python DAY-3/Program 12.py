num = int(input("enter a number1:"))
seen_numbers = set()

while num != 1 and num not in seen_numbers:
    seen_numbers.add(num)
    num = sum(int(digit) ** 2 for digit in str(num))

if num == 1:
    print(f"{num} is a happy number")
else:
    print(f"{num} is not a Happy number")
