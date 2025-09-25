# ===================================================================================
# Chapter 7: Arithmetic Operators
#
# This guide covers the fundamental operators used for performing mathematical
# calculations in Python. It also explores the critical concept of operator
# precedence, which dictates the order of operations.
#
# Author:         Mojtaba Akbarzadeh Saghaei
# GitHub Profile: https://github.com/akbarzadehmojtabasaghaei-del/python-basics
# LinkedIn:       https://www.linkedin.com/in/mojtaba-akbarzadeh-saghaei
# ===================================================================================


# ===================================================================================
# ## Level 1: Basic Arithmetic Operators
# The essential tools for any numerical task.
# ===================================================================================

# Your excellent practice code:
x = 4
y = 5

# --- Topic: Addition, Subtraction, Multiplication ---
z = x + y  # Addition -> 9
s = x - y  # Subtraction -> -1
a = x * y  # Multiplication -> 20
print(f"Sum: {z}, Difference: {s}, Product: {a}")

# --- Topic: Division Operators ---
# Python provides three different types of division.

# 1. True Division (`/`): Always returns a float.
q = x / y  # -> 0.8
print(f"True Division (/): {q}")

# 2. Floor Division (`//`): Divides and rounds *down* to the nearest whole number.
r = x // y # -> 0
print(f"Floor Division (//): {r}")
print(f"Example with positive result: 14 // 3 = {14 // 3}") # -> 4

# 3. Modulo (`%`): Returns the remainder of a division.
w = x % y  # -> 4 (4 divided by 5 is 0 with a remainder of 4)
print(f"Modulo/Remainder (%): {w}")
print(f"Example: 14 % 3 = {14 % 3}") # -> 2

# --- Topic: Exponentiation (Power) ---
e = x ** y # Same as 4^5 -> 1024
print(f"Exponent (**): {e}")


# ===================================================================================
# ## Level 2: Operator Precedence
# Understanding the order in which Python evaluates expressions.
# ===================================================================================

# --- Topic: The Order of Operations (PEMDAS) ---
# Python follows this order: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.

# Your exploration of precedence:
# Let's break down `x // y ** z` (with x=4, y=5, z=9)
# 1. Exponent is calculated first: `y ** z` -> `5 ** 9` -> 1953125
# 2. Then Floor Division: `x // 1953125` -> `4 // 1953125` -> 0
result_precedence = x // y ** z
print(f"\nResult of 'x // y ** z' is: {result_precedence}")

# --- Topic: Using Parentheses for Clarity ---
# BEST PRACTICE: Use parentheses to make the order of operations explicit and readable.

# AMBIGUOUS (but works):
# Does the programmer want (z+x)+x or z+(x+x)?
ambiguous_result = z + x + x

# CLEAR AND EXPLICIT:
clear_result = z + (x + x)
print(f"Ambiguous result: {ambiguous_result}, Clear result: {clear_result}")


# ===================================================================================
# ## Level 3: Augmented Assignment Operators
# A concise, Pythonic shortcut for modifying variables.
# ===================================================================================

# --- Topic: Shorthand Operators ---
# These operators combine an arithmetic operation with an assignment.

# STANDARD WAY:
score = 100
score = score + 10 # -> 110

# PYTHONIC WAY (more readable and efficient):
score += 10 # Same as score = score + 10
print(f"\nUpdated score: {score}")

# This works for all arithmetic operators:
# -=, *=, /=, //=, %=, **=
level = 5
level *= 2 # level is now 10
print(f"Player level: {level}")


print("\n--- Arithmetic Operators Mastery Guide: Complete ---")