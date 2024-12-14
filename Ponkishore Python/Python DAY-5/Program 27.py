def is_composite(n):
    if n < 4:  # The smallest composite number is 4
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

def print_composite_numbers(a, b):
    print(f"Composite numbers between {a} and {b}:")
    for num in range(a, b + 1):
        if is_composite(num):
            print(num)

# Example usage
a = 10
b = 30
print_composite_numbers(a,b)
