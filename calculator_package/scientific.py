"""This module contain the calculator subclass with more scientific operations
(power, square root, modulo and factorial)."""

from calculator_package.basic import Calculator
from math import sqrt, factorial

class ScientificCalculator(Calculator):
    """
    Scientific calculator with more complex operations like power, square root, 
    modulo and factorial.
    """
    def __init__(self) -> None:
        """
        Initialize class atributes
        
        """
        super().__init__()

    def power(self, a: float, b: float) -> float:
        """
        Elevate number a at b power 
        
        a: Number to elevate
        type a: float
        b: Number of power
        b: float
        :return: a at the b power
        :rtype: float
        """
        self.history.append(f"{a:.2f} ** {b:.2f} = {(a ** b):.2f}")
        return a ** b
    
    def modulo(self, a: float, b: float):
        """
        Calculation of the remainder of a divided by b
        
        param a: Numerator
        :type a: float
        :param b: Denominator
        :type b: float
        :return: Remainder or error message (ZeroDivisionError)
        :rtype: float or Exception object
        """
        try:
            result = a % b
            self.history.append(f"{a:.2f} % {b:.2f} = {result:.2f}")
        except ZeroDivisionError:
            return Exception("Oops.. Division by 0 impossible!")
        return result
    
    def square_root(self, a: float):
        """
        Calculation of a square root
        
        a: Number on we want apply square root
        type a: float
        return: Square root of a
        rtype: float
        """
        try:
            result = sqrt(a)
            self.history.append(f"sqrt({a:.2f}) = {result:.2f}")
        except ValueError:
            return Exception(
                "Oops.. square root of a negative number impossible!"
                )
        return result
    
    def factorial_number(self, a: int):
        """
        Calculation of a factorial
        
        param a: Factorial number
        type a: int
        return: a factorial
        :rtype: int
        """
        try:
            result = factorial(int(a))
            self.history.append(f"{int(a)}! = {result}")
        except ValueError:
            return Exception("Oops.. factorial of negative number impossible!")
        return result