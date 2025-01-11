from arithmetic_operations import perform_operation
from shopping_list_manager import display_menu
from datetime import datetime, timedelta
from temp_conversion_tool import convert_to_celsius, convert_to_fahrenheit

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()