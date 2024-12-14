a = int(input("Enter the first binary number: "), 2)
b = int(input("Enter the second binary number: "), 2)
c = int(input("Enter the third binary number: "), 2)

greatest = max(a, b, c)
print(f"The greatest number is: {bin(greatest)[2:]}")
