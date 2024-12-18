task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a high-priority task. Handle it immediately!")
        elif time_bound == "no":
            print(f"'{task}' is a high-priority task but not time-sensitive.")
        else:
            print("Invalid input for time-bound. Please enter 'yes' or 'no'.")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a medium-priority task. Address it soon.")
        elif time_bound == "no":
            print(f"'{task}' is a medium-priority task with no urgent deadline.")
        else:
            print("Invalid input for time-bound. Please enter 'yes' or 'no'.")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a low-priority task that can be scheduled later.")
        elif time_bound == "no":
            print(f"'{task}' is a low-priority task with no immediate deadline.")
        else:
            print("Invalid input for time-bound. Please enter 'yes' or 'no'.")
