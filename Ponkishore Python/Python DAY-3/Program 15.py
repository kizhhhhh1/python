number = input("enter a number1:")
permutations = []

for i in range(len(number)):
    for j in range(len(number)):
        if i != j:
            perm = number[i] + number[j] + "".join(k for k in number if k != number[i] and k != number[j])
            if perm not in permutations:
                permutations.append(perm)

for perm in permutations:
    print(perm)
