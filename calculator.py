def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("Enter choice (1/2/3/4 or +, -, *, /): ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if choice in ('1', '+'):
        result = add(num1, num2)
    elif choice in ('2', '-'):
        result = subtract(num1, num2)
    elif choice in ('3', '*'):
        result = multiply(num1, num2)
    elif choice in ('4', '/'):
        result = divide(num1, num2)
    else:
        print("Invalid operation selected.")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
