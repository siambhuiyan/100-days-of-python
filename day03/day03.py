a = 200
b = 100
c = 50

if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("a is less than b")

if(a>b) and (b>c):
    print("a is greater than b and b is greater than c")
elif(a>b) and (b<c):
    print("a is greater than b and b is less than c")
elif(a<b) or (b>c):
    print("a is less than b and b is greater than c")

# short hand if
print('a is bigger than b') if a>b else print('a is smaller than b')

print(f"value of a is ${a}")