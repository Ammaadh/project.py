"""
Simple CLI Utility: Calculator & Unit Converter
"""

def show_menu():
    print("\n=== SIMPLE MULTI-TOOL CALCULATOR ===")
    print("1. Standard Arithmetic (Add, Subtract, Multiply, Divide)")
    print("2. Temperature Conversion (Celsius <-> Fahrenheit)")
    print("3. Distance Conversion (Kilometers <-> Miles)")
    print("4. Exit")

def arithmetic_calculator():
    print("\n--- Arithmetic Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))
        
        if op == '+':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif op == '-':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif op == '*':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid operator selected.")
    except ValueError:
        print("Error: Please enter valid numbers.")

def temperature_converter():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose option (1 or 2): ").strip()
    
    try:
        if choice == '1':
            c = float(input("Enter temperature in Celsius: "))
            f = (c * 9/5) + 32
            print(f"{c}°C is equal to {f:.2f}°F")
        elif choice == '2':
            f = float(input("Enter temperature in Fahrenheit: "))
            c = (f - 32) * 5/9
            print(f"{f}°F is equal to {c:.2f}°C")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Error: Please enter a valid number.")

def distance_converter():
    print("\n--- Distance Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = input("Choose option (1 or 2): ").strip()
    
    try:
        if choice == '1':
            km = float(input("Enter distance in Kilometers: "))
            miles = km * 0.621371
            print(f"{km} km is equal to {miles:.2f} miles")
        elif choice == '2':
            miles = float(input("Enter distance in Miles: "))
            km = miles / 0.621371
            print(f"{miles} miles is equal to {km:.2f} km")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == '1':
            arithmetic_calculator()
        elif choice == '2':
            temperature_converter()
        elif choice == '3':
            distance_converter()
        elif choice == '4':
            print("\nGoodbye!")
            break
        else:
            print("Invalid selection, please choose between 1 and 4.")

if __name__ == "__main__":
    main()
