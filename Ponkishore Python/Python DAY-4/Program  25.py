a = input("enter the first binary string: ")
b = input("Enter the second binary string: ")
sum_binary = bin(int(a, 2) + int(b, 2))[2:]
print(f"The sum is {sum_binary}")
