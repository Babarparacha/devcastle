try:
    # Attempting to divide by zero (which Python hates)
    result = 10 / 0
    print(result)

except ZeroDivisionError:
    # This block catches the specific error and handles it safely
    print("Error: Division by zero is not allowed.")
    
finally:
    # This always runs, useful for closing files or connections
    print("Execution of try-except block is complete.")

