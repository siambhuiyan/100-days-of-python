import random

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']


n_letter = int(input("How many letters would you like in your password? "))
n_number = int(input("How many numbers would you like in your password? "))
n_symbol = int(input("How many symbols would you like in your password? "))


password = ""


for char in range (1, n_letter + 1):
    password += random.choice(letter)

for char in range (1, n_number + 1):
    password += random.choice(number)

for char in range (1, n_symbol + 1):
    password += random.choice(symbol)

print(f"Your password is: {password}")