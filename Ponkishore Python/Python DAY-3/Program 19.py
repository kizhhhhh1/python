number = float(input("enter a decimal number1:"))
operation = input("enter 'square' to find the square or 'cube' to find the cube:").strip().lower()

if operation == "square":
    result = number ** 2
    print(f"The square of {number} is {result}")
elif operation == "cube":
    result = number ** 3
    print(f"The cube of {number} is {result}")
else:
    print("Invalid operation")
