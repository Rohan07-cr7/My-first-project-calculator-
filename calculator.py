# calculator.py

def add(x, y):
    """Adds two numbers and returns the sum."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers and returns the difference."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers and returns the product."""
    return x * y

def divide(x, y):
    """Divides two numbers and returns the quotient. Handles division by zero."""
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def get_numbers():
    """Prompts the user for two numbers and returns them as floats."""
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def display_menu():
    """Displays the operation menu to the user."""
    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

def main():
    """Main function to run the calculator application."""
    while True:
        display_menu()
        choice = input("Enter choice (1/2/3/4/5): ")
