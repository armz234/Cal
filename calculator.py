num1 = input("Enter your number")
num2 = input("Enter your second number")
new_num1 = int(num1)
new_num2 = int(num2)
operation = input("operation [+, -]: ")

if operation == "+":
    combination = new_num1 + new_num2
elif operation == "-":
    combination = new_num1 - new_num2
else:
    print("Error: 404")

newcomb = str(combination)
print ("Answer:" + newcomb)
