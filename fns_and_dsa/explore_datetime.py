from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

display_current_datetime()

def calculate_future_date():
    days_to_add = input('Enter the number of days to add to the current date: ')
    
    # Ensure the input is a valid integer
    while not days_to_add.isdigit():
        print("Invalid input. Please enter a positive integer.")
        days_to_add = input('Enter the number of days to add to the current date: ')
    
    # Convert the validated input to an integer
    days_to_add = int(days_to_add)
    future_date = datetime.now() + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

calculate_future_date()