# ===================================================================================
# Chapter 10: Logical Operators (and, or, not)
#
# This guide covers the logical operators that are fundamental for creating
# complex conditions and controlling the flow of a program. They work with
# Boolean values to produce a single Boolean result.
#
# Author:         Mojtaba Akbarzadeh Saghaei
# GitHub Profile: https://github.com/akbarzadehmojtabasaghaei-del/python-basics
# ===================================================================================

x = 4
y = 5
z = 4

# --- Topic: The `and` Operator ---
# Returns `True` only if *all* conditions are true.
print(f"Result of (x < 3 and y > 1): {x < 3 and y > 1}") # False and True -> False
print(f"Result of (x > 0 and x == z): {x > 0 and x == z}") # True and True -> True

# --- Topic: The `or` Operator ---
# Returns `True` if *at least one* condition is true.
print(f"Result of (z < 2 or x > 2): {z < 2 or x > 2}") # False or True -> True
print(f"Result of (x > 50 or y > 100): {x > 50 or y > 100}") # False or False -> False

# --- Topic: The `not` Operator ---
# Inverts the Boolean value of a condition.
is_admin = False
print(f"Is user an admin? {is_admin}")
print(f"Is user NOT an admin? {not is_admin}") # not False -> True

# Combining `not` with other operators:
print(f"Original: (x < 3 and y > 1) -> {x < 3 and y > 1}") # -> False
print(f"Negated: not(x < 3 and y > 1) -> {not(x < 3 and y > 1)}") # not False -> True

print("\n--- Logical Operators Mastery Guide: Complete ---")