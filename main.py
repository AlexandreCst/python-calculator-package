"""
Script that give to the user the possibility of make basic operations untill it
decide to quit. He has the possibility to display his history of each operation
done.
"""

from calculator_package import ScientificCalculator
from calculator_package import get_valid_operation, get_valid_number, check_quit
from calculator_package import handle_error

def main():
    """Calculator script."""
    print("===================================================================")
    print("====================== SCIENTIFIC CALCULATOR ======================")
    print("===================================================================")
    print("\nEnter 'q' at anytime to quit.\n")

    calculation = ScientificCalculator() # Create a calculator
    while True:
        # Check if the inputs is valid for numbers (int or float)
        first_number = get_valid_number("Enter a number: ", calculation)

        # Check if the operation is valid (+, -, *, /, **, %, sqrt, !)
        operation = get_valid_operation(
            "\nWhat operation (+, -, *, /, **, %, sqrt, !) do you want to do? ",
            calculation
            )
        
        # Make operations which only used to one number
        if operation in ["sqrt", "!"]:
            if operation == "sqrt":
                square_root = calculation.square_root(first_number)
                handle_error(square_root)
            else:
                factor = calculation.factorial_number(int(first_number))
                handle_error(factor)      
        
        else:
            # Make operations which need 2 numbers
            second_number = get_valid_number(
                "Enter a second number: ",
                calculation
                )

            # Make the appropriate operation demand by the user
            if operation == "+":
                add = calculation.addition(first_number, second_number)
                print(f"\nResult: {add:.2f}")
            
            elif operation == "-":
                sub = calculation.subtraction(first_number, second_number)
                print(f"\nResult: {sub:.2f}")
            
            elif operation == "*":
                mul = calculation.multiplication(first_number, second_number)
                print(f"\nResult: {mul:.2f}")

            elif operation == "**":
                power = calculation.power(first_number, second_number)
                print(f"\nResult: {power:.2f}")
            
            elif operation == "%":
                modulo = calculation.modulo(first_number, second_number)
                handle_error(modulo)

            else:
                div = calculation.division(first_number, second_number)
                handle_error(div)
        

        # Ask if the user wishes to display its history
        user_history = input("\nDo you want to show your history? (y/n)")

        # Check if the user want to quit
        user_quit = check_quit(user_history, calculation)

        # Display the history
        if user_history.lower().strip() in ['y', 'yes']:
            calculation.show_history()



if __name__ == "__main__":
    main()
    

