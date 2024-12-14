number = int(input("enter the number1:"))
n = int(input("enter the factor position(n):"))

factors = [i for i in range(1, number + 1) if number % i == 0]

print(f"Total number of factors are {len(factors)}")

if n <= len(factors):
    print(f"The {n}th factor is {factors[n - 1]}")
else:
    print(f"The {n}th factor does not exist")
