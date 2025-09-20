# Filename: docstring_practice.py
# Author:Mojtaba Akbarzadeh 
# Date: 2025-09-20
# Description: This script provides a clear example of how to use
#              module-level and function-level docstrings in Python.

"""
This is a module-level docstring.

It explains the purpose of the entire file. This script demonstrates
the proper use of docstrings for documenting functions according to PEP standards.
"""

def add_two_numbers(num1, num2):
  """Calculates the sum of two numbers.

  This function takes two numbers as arguments, adds them together,
  and returns the result. It is a simple demonstration of a well-documented
  function.

  Args:
    num1 (int or float): The first number to be added.
    num2 (int or float): The second number to be added.

  Returns:
    int or float: The sum of num1 and num2.
  """
  # The core logic is to simply use the '+' operator.
  result = num1 + num2
  return result

# --- Main execution block ---
# The following code will only run when this script is executed directly.
if __name__ == "__main__":
  # Example usage of the function
  number_a = 15
  number_b = 10
  sum_result = add_two_numbers(number_a, number_b)

  print(f"The sum of {number_a} and {number_b} is: {sum_result}")