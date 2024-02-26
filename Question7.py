import random
random_numbers = []

for i in range(10):
    random_numbers.append(random.randint(1, 100))
    if random_numbers[i] % 2 != 0:
        random_numbers[i] = 0
    else:
        random_numbers[i] = random_numbers[i] * 2
#remove the zeros
random_numbers = [x for x in random_numbers if x != 0]
print(random_numbers)