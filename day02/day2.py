# Data types 

print("hello"[1]); # e
print("hello"[-1]); # o
print("hello"[0:3]); # hel

print(len('hell')); # 4
print(len('hello world')); # 11
print(len('')); # 0

print("Number of letters in your name: " + str(len(input("Enter your name: ")))); # Number of letters in your name: 4

height = 122.5;
weight = 70.5;

bmi = weight / (height ** 2); # height in meters

print(f"Your BMI is {bmi:.2f}"); # Your BMI is 0.47