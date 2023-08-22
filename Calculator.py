def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

operations = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide
}

while True:
    print("Simple Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    operation = input("Select operation (1/2/3/4/5): ")

    if operation == '5':
        print("Calculator exiting. Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    selected_operation = operations.get(operation)

    if selected_operation:
        result = selected_operation(num1, num2)
        operator = "+-*/"[int(operation) - 1]
        print(f"{num1} {operator} {num2} = {result}")
    else:
        print("Invalid operation")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        print("Calculator exiting. Goodbye!")
        break
