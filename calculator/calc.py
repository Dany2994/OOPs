#Function definition
def sum(a, b):
    return a+b

def subs(a, b):
    return a-b

def multiply(a, b):
    return a*b

def division(a, b):
    if b !=0:
        return a/b
    else:
        return "Division not allowed"
    
def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid INTEGER number")
    
def main():
    print("Select operation: ")
    print("1. Sum")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")

operation = input("Select operation: (1/2/3/4): ")

num1 = float(input("Type the first number (INTEGERS ONLY): "))
num2 = float(input("Type the second number (INTEGERS ONLY): "))

if operation == "1":
    print("Result: ", sum(num1, num2))
elif operation == "2":
    print("Result: ", subs(num1, num2))
elif operation == "3":
    print("Result: ", multiply(num1, num2))
elif operation == "4":
    print("Result: ", division(num1, num2))

main()