FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temperature_input = float(input("Enter the temperature to convert: "))
    if not temperature_input.replace('.', '', 1).isdigit():
        print("Invalid temperature. Please enter a numeric value.")
        return 
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if unit == 'C':
        fahrenheit = convert_to_fahrenheit(temperature_input)
        print(f"{temperature_input}°C is {fahrenheit}°F")
    elif unit == 'F':
        celsius = convert_to_celsius(temperature_input)
        print(f"{temperature_input}°F is {celsius}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
if __name__ == "__main__":
    main()