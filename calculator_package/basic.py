"""This module contain the clasic calculator class (addition,
 subtraction, mulitplication and division)."""

from pathlib import Path

class Calculator:
    """This class represent a calculator with basic operations"""
    
    def __init__(self) -> None:
        """Initialize class attributes"""
        self.history = []

    def addition(self, a: float, b: float) -> float:
        """
        Addition of 2 terms a and b 
        
        Append the operation and result to the history.
        
        a: float
        b: float
        return type: float"""
        self.history.append(f"{a:.2f} + {b:.2f} = {a + b:.2f}")
        return a + b
    
    def subtraction(self, a: float, b: float) -> float:
        """
        Subtraction of 2 terms a and b

        Append the operation and result to the history.
        
        a: float
        b: float
        return type: float"""
        self.history.append(f"{a:.2f} - {b:.2f} = {a - b:.2f}")
        return a - b
    
    def multiplication(self, a: float, b: float) -> float:
        """
        Multiplication of 2 terms a and b

        Append the operation and result to the history.
        
        a: float
        b: float
        return type: float
        """
        self.history.append(f"{a:.2f} * {b:.2f} = {a * b:.2f}")
        return a * b
    
    def division(self, a: float, b: float):
        """
        Divsion of 2 terms a by b
        
        Append the operation and result to the history.

        a: float
        b: float
        return type: float
        """
        try:
            result = a / b
            self.history.append(f"{a:.2f} / {b:.2f} = {a / b:.2f}")
        except ZeroDivisionError:
            return Exception("Oops.. Division by 0!")
            
        return result
    
    def show_history(self):
        """
        Display the calculation history
        """
        if self.history == []:
            print("Ooh non history is empty.. Make an operation!")
        else:
            for operation in self.history:
                print(operation)

    
    def clear_history(self):
        """
        Clear the calculation history
        """
        self.history = []

    def save_history(self, filename, format="txt"):
        """
        Save the calculation history in a file
        """
        full_filename = f"{filename}.{format}"
        path = Path(full_filename)
        try:
            path.write_text('\n'.join(self.history), encoding='utf-8')
        except Exception:
            return None
        return full_filename
    
    def load_history(self, filename, format="txt"):
        """
        Give the possibility to load the history directly from a file
        """
        path = Path(f"{filename}.{format}")

        try: # Check if the file exist and add lines in history
            history_contents = path.read_text()
            lines = history_contents.splitlines()
            for line in lines:
                self.history.append(line)
        
        except FileNotFoundError: # If the file doesn't exist or not found
            return None 
        
        return len(lines) # Number of lines added in history