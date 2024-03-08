import random

def generate_random_numbers():
    return [random.randint(1, 100) for _ in range(20)]

random_numbers = generate_random_numbers()
print(random_numbers)