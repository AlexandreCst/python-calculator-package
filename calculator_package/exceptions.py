"""This module define custom exceptions"""

class CalculatorError(Exception):
    """Main class to define custom exceptions."""
    pass


class InvalidOperationError(CalculatorError):
    """Custom exception to invalid operation."""
    pass

class HistoryEmptyError(CalculatorError):
    """Custom exception for empty history."""
    pass