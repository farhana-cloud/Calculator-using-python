# Simple Calculator Program

# Function to perform calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operation!"

# Main program
print("Simple Calculator")
print("Operations: +  -  *  /")

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose an operation (+, -, *, /): ")

# Perform calculation
result = calculate(num1, num2, operation)

# Display result
print("Result:", result)
