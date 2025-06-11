import sys
from src.logger import logging

def error_message_details(error, error_detail:sys):
    """
    Extracts the error message and details from an exception.
    
    Args:
        error (Exception): The exception object.
        error_details (sys): The sys module to access exc_info.
    
    Returns:
        str: A formatted string containing the error message and details.
    """
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self,error_message, error_detail:sys):
        """
        Custom exception class to handle exceptions with detailed messages.
        
        Args:
            error_message (str): The error message to be displayed.
            error_details (sys): The sys module to access exc_info.
        """
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details = error_detail)

    def __str__(self):
        """
        Returns the string representation of the custom exception.
        
        Returns:
            str: The detailed error message.
        """
        return self.error_message