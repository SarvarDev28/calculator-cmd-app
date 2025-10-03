# This is a test for Github

operation = 0
operations = ["+", "-", "*", "/"]

while operation not in operations:
    operation = (input("Please, choose mathematic operation: +, -, *, /:  "))

x1 = (input("Please, enter your first number: "))
while not x1.isdigit():
    print("Faqat son kiriting!")
    x1 = (input("Please, enter your first number: "))
    exit
x2 = (input("Please, enter your second number: "))
while not x2.isdigit():
    print("Faqat son kiriting!")
    x2 = (input("Please, enter your second number: "))
    exit

x1 = int(x1)
x2 = int(x2)
    
if operation == "+":
    print(x1 + x2)
elif operation == "-":
    print(x1 - x2)
elif operation == "*":
    print(x1 * x2)
elif operation == "/":
    print(x1 / x2)
