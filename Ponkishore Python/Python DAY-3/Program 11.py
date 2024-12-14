number = int(input("enter the number1:"))
n = int(input("enter the number of factors to display:"))

factors = [i for i in range(1, number + 1) if number % i == 0]

print(f"Total number of factors are {len(factors)}")
print(f"First {n} factors is {factors[:n]}")
