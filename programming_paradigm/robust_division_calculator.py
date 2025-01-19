def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Invalid input"
    finally:
        print("Safe division operation completed.")
