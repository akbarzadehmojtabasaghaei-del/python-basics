# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Chapter 15: The Definitive Guide to Operator Precedence
#
# This guide provides a comprehensive and example-rich look at the order of
# operations in Python. While the language has a strict hierarchy, the most
# professional and readable code always uses parentheses `()` to make the
# evaluation order explicit.
#
# Author:         Mojtaba Akbarzadeh Saghaei
# GitHub Profile: https://github.com/akbarzadehmojtabasaghaei-del/python-basics
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

print("--- Level 18-15: The Highest Precedence (Grouping, Calls, Access) ---")
# `()` Parentheses, `f()` Function Calls, `[]` Slicing/Subscription
# These are evaluated first to determine the objects for other operations.
my_list = [10, 20, 30, 40]
# Slicing `my_list[1:3]` happens first, resulting in `[20, 30]`.
# Then the `sum()` function is called on that new list.
result = sum(my_list[1:3]) + 5
print(f"Result of sum(my_list[1:3]) + 5 is: {result}") # sum([20, 30]) + 5 -> 50 + 5 -> 55

print("\n--- Level 14: `**` (Exponentiation) ---")
# This is the highest mathematical operator. It's right-associative.
# Example 1: Basic precedence
result = 100 - 2 ** 4  # 2 ** 4 (16) is calculated first. Then 100 - 16.
print(f"100 - 2 ** 4 = {result}") # -> 84

# Example 2: Right-associativity
result = 2 ** 3 ** 2 # Interpreted as 2 ** (3 ** 2) -> 2 ** 9
print(f"2 ** 3 ** 2 = {result}") # -> 512

print("\n--- Level 13-12: Unary Operators (`+x`, `-x`, `~x`) ---")
# These operators act on a single operand.
result = -5 ** 2 # Exponentiation (**) has higher priority than unary minus (-).
                 # So, this is `-(5 ** 2)`.
print(f"-5 ** 2 = {result}") # -> -25

result = (-5) ** 2 # Using parentheses changes the order.
print(f"(-5) ** 2 = {result}") # -> 25

result = ~10 + 3 # Bitwise NOT (~) is done first. `~10` is `-11`. Then `-11 + 3`.
print(f"~10 + 3 = {result}") # -> -8

print("\n--- Level 11: `*`, `/`, `//`, `%` (Multiplication & Division Group) ---")
# This group has the same priority and is evaluated from left to right.
result = 100 / 10 * 2 # 100 / 10 (10.0) is first. Then 10.0 * 2.
print(f"100 / 10 * 2 = {result}") # -> 20.0

result = 25 % 7 // 2 # 25 % 7 (4) is first. Then 4 // 2.
print(f"25 % 7 // 2 = {result}") # -> 2

print("\n--- Level 10: `+`, `-` (Addition & Subtraction) ---")
# Lower priority than the multiplication group.
result = 10 + 5 * 3 # 5 * 3 (15) is first. Then 10 + 15.
print(f"10 + 5 * 3 = {result}") # -> 25

result = 8 - 4 * 2 + 10 / 5 # 4*2 (8) and 10/5 (2.0) are first.
                            # Then 8 - 8 + 2.0 -> 0 + 2.0
print(f"8 - 4 * 2 + 10 / 5 = {result}") # -> 2.0

print("\n--- Level 9-8: `<<`, `>>` (Bitwise Shifts) ---")
# Evaluated after the main arithmetic operators.
result = 5 + 2 << 1 # 5 + 2 (7) is first. Then 7 << 1 (binary 111 becomes 1110).
print(f"5 + 2 << 1 = {result}") # -> 14

result = 32 >> 1 + 1 # 1 + 1 (2) is first. Then 32 >> 2 (binary 100000 becomes 1000).
print(f"32 >> 1 + 1 = {result}") # -> 8

print("\n--- Level 7-5: `&`, `^`, `|`, Comparisons (`in`, `is`, `==`, `>`) ---")
# This is a large group where comparisons and bitwise logic are evaluated.
# Example 1:
result = 5 > 3 & 2 > 1 # 5 > 3 (True) and 2 > 1 (True). Then `True & True`.
                      # In bitwise context, True is 1, False is 0. So `1 & 1`.
print(f"5 > 3 & 2 > 1 = {result}") # -> 1 (which is considered True)

# Example 2 (clearer with parentheses):
result = (5 > 3) and (2 > 1)
print(f"(5 > 3) and (2 > 1) = {result}") # -> True (This is the recommended way)

# Example 3:
result = 4 | 3 > 1 # 3 > 1 (True) is first. Then 4 | True -> 4 | 1.
                   # 4 is 100, 1 is 001. 100 | 001 -> 101
print(f"4 | 3 > 1 = {result}") # -> 5

print("\n--- Level 4-2: `not`, `and`, `or` (Logical Operators) ---")
# These have the lowest precedence, for combining boolean expressions.
# Their internal order is `not` -> `and` -> `or`.
# Example 1:
result = True or True and False # `True and False` (False) is first. Then `True or False`.
print(f"True or True and False = {result}") # -> True

# Example 2:
result = not False and True or False # `not False` (True) is first.
                                     # Then `True and True` (True).
                                     # Then `True or False`.
print(f"not False and True or False = {result}") # -> True

# Example 3: The Golden Rule - Use Parentheses for Clarity!
clear_result = (not False) and (True or False) # `not False` (True), `True or False` (True).
                                               # `True and True`
print(f"(not False) and (True or False) = {clear_result}") # -> True


print("\n--- Operator Precedence Mastery Guide: Complete ---")