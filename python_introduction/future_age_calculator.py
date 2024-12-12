# Asking for users age
def Current_age():
    while True:
        try:
            # Prompt the user for their current age
            current_age = int(input("How old are you? "))
            return current_age
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

present_age = Current_age()

# Calculating their future age
age = present_age + 27
print(f"In 2050, you will be {age} years old")