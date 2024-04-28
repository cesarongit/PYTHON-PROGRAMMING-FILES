ch = str(input("Enter the operation - + - * /"))
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")
print(num1, ch , num2, ":", result)