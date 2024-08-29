# Function to perform the calculation
def calculate(num1, num2, operation):
    if (operation == 'add') or (operation == '+') :
        return num1 + num2
    elif (operation == 'subtract') or (operation == '-'):
        return num1 - num2
    elif (operation == 'multiply') or (operation == '*'):
        return num1 * num2
    elif (operation == 'divide') or (operation == '/'):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

# Main function to handle user input and display result
def main():
    print("****************** Simple Calculator ******************")
    
    # Input from user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Choose an operation: add, subtract, multiply, divide")
    operation = input("Enter operation: ").strip().lower()
    
    # Calculate result
    result = calculate(num1, num2, operation)
    
    # Display result
    print(f"Result: {result}")

# Run the calculator
if __name__ == "__main__":
    main()
