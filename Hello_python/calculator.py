
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# # Returns only whole number
# # result = int(num1) + int(num2)
#
# # float uses both decimals and whole numbers
# result = float(num1) + float(num2)
# print(result)

# Better Calculator!
num5 = float(input("Enter first number: "))
op = input("Enter operator: ")
num6 = float(input("Enter second number: "))

if op == "+":
    print(num5+num6)
elif op == "-":
    print(num5-num6)
elif op == "/":
    print(num5/num6)
elif op == "*":
    print(num5*num6)
else:
    print("Invalid operator")