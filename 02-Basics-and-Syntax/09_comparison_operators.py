# ===================================================================================
# Chapter 8: Comparison Operators
#
# This guide covers the operators used to compare values in Python. These
# operators are the foundation of decision-making and control flow, as their
# result is always a Boolean value (`True` or `False`).
#
# Author:         Mojtaba Akbarzadeh Saghaei
# GitHub Profile: https://github.com/akbarzadehmojtabasaghaei-del/python-basics
# LinkedIn:       www.linkedin.com/in/mojtaba-akbarzadeh-saghaei
# ===================================================================================


# ===================================================================================
# ## Level 1: Basic Comparison Operators
# These operators compare two values and return a Boolean.
# ===================================================================================

x = 4
e = 5

# --- Topic: Equality and Inequality ---
# `==` (Equal): Checks if two values are equal.
# `!=` (Not Equal): Checks if two values are *not* equal.

print(f"Is x equal to 5? (x == 5) -> {x == 5}")       # False
print(f"Is x not equal to 5? (x != 5) -> {x != 5}")   # True

# PROFESSIONAL ADVICE: A common beginner mistake is using `=` (assignment)
# instead of `==` (comparison) in an `if` statement.
# WRONG: if x = 4: ...
# CORRECT: if x == 4: ...


# --- Topic: Greater Than / Less Than ---
# `>` (Greater than)
# `<` (Less than)
# `>=` (Greater than or equal to)
# `<=` (Less than or equal to)

print(f"Is x greater than 4? (x > 4) -> {x > 4}")     # False
print(f"Is x less than e? (x < e) -> {x < e}")       # True
print(f"Is x less than or equal to e? (x <= e) -> {x <= e}") # True


# ===================================================================================
# ## Level 2: Chained Comparisons
# A clean, Pythonic way to write complex comparisons.
# ===================================================================================

# --- Topic: How Chaining Works ---
# Python allows you to chain comparison operators for better readability.

# Example 1: Checking if a value is within a range.
# This is the Pythonic way to check if x is between 2 and 9.
print(f"Is x between 2 and 9? (2 < x < 9) -> {2 < x < 9}") # True
# This is interpreted as: `(2 < x) and (x < 9)`

# Example 2: Your interesting test case.
print(f"Result of (3 < x > 8): {3 < x > 8}") # False
# This is interpreted as: `(3 < x) and (x > 8)`
# Which is `(3 < 4) and (4 > 8)` -> `True and False` -> `False`


# ===================================================================================
# ## Level 3: A Note on Bitwise Operators
# A brief introduction to operators that work on a different level.
# ===================================================================================

# --- Topic: Bitwise Shift Operators (`<<`, `>>`) ---
# In your practice, you used `<<` and `>>`. These are NOT comparison operators.
# They are **Bitwise Shift Operators**.

# They work on the binary representation of numbers. For example, `x = 4` in binary is `100`.
# `x << 2` means "shift the bits of x to the left by 2 places", resulting in `10000` (which is 16).
# `x >> 2` means "shift the bits of x to the right by 2 places", resulting in `1` (which is 1).

# PROFESSIONAL ADVICE: These are advanced operators used in specific domains like
# networking, cryptography, or high-performance computing. We will dedicate a
# separate, detailed chapter to them later in our journey.


print("\n--- Comparison Operators Mastery Guide: Complete ---")