print("welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "));
people = int(input("How many people to split the bill? "));

total =bill + (tip/100 * bill);

total_per_person = total / people;

print(f"total bill is ${total: .2f}")
print(f"total per person is ${total_per_person: .2f}")