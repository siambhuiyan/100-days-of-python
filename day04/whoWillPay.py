import random

name = [ 'Angela', 'James', 'Liam', 'Emma', 'Olivia', 'Noah', 'Ava', 'Sophia', 'Isabella', 'Charlotte']
print(len(name))

random_choice = random.choice(name)
print(f'{random_choice} is going to buy the meal today!')