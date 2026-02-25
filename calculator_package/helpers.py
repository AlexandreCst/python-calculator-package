"""This module contain some utils function."""

from calculator_package.basic import Calculator

def quit_and_save(calculation: Calculator):
    """Check if history is not empty and save the history inside a file"""
    if calculation.history == []:
        exit()
    else:
        filename = calculation.save_history("history", format='txt')
        print(f"\nYour history is available inside the {filename} file.")
        exit()


def check_quit(user_input: str, calculation: Calculator):
    """
    Check if the user want to quit the calculator
    
    user_input: Message displaying to the user
    type user_input: str
    return: The value enter by the user
    rtype: str
    """
    if user_input.lower().strip() in ['q', 'quit']:
        quit_and_save(calculation)
    else:
        return user_input

def get_valid_number(prompt_message: str, calculation: Calculator) -> float:
    """
    Check if the user input is a valid number and return this value converting
    in float
    
    prompt_message: Message displaying to the user
    type prompt_message: str
    return: The value enter by the user converted in float
    rtype: float
    """
    while True:
        user_input = input(prompt_message)
        check_quit(user_input, calculation) # Check if the user want to quit
        try:
            user_prompt = float(user_input)
            break
        except (ValueError, TypeError):
            print("Sorry the value isn't valid.. Please enter a number.")
            continue
    return user_prompt

def get_valid_operation(prompt_message: str, calculation: Calculator) -> str:
    """
    Check if the user input is a valid operation and return it
    
    prompt_message: Message displaying to the user
    type prompt_message: str
    return: The valid operation
    rtype: str
    """
    while True:
        operation = input(prompt_message)
        check_quit(operation, calculation) # Check if the user want to quit
        if operation not in ["+", "-", "*", "/", "**", "%", "sqrt", "!"]:
            print("Please, enter a valid operation..")
            continue
        else:
            break
    return operation

def handle_error(operation):
    """
    Function to handle error that can be occur in operations like modulo (%), 
    factorial (!), division (/), square root (sqrt).
    
    operation: Operation that user want to apply
    type operation: float, int or Exception object
    """
    if isinstance(operation, Exception): 
        print(f"\n{operation}") # Display error message
    else: # If it's valid
        print(f"\nResult: {operation:.2f}")