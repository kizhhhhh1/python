n = int(input("enter the number of elements:"))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]

gcd = numbers[0]
for num in numbers[1:]:
    a, b = gcd, num
    while b:
        a, b = b, a % b
    gcd = a

lcm = numbers[0]
for num in numbers[1:]:
    lcm = (lcm * num) // gcd

print(f"GCD of the numbers is {gcd}")
print(f"LCM of the numbers is {lcm}")
