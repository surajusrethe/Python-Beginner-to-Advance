a = int(input("Enter your 1st number: "))
b = int(input("Enter your 2nd number: "))
op = input("Enter Operator")

if op == "+":
    print("The addition is ", a+b)
elif op == "-":
    print("The substraction is ", a-b)
elif op == "*":
    print("The multiplication is ", a*b)
elif op == "/":
    print("The division is ", a/b)
else:
    print(" Invalid Operation ")