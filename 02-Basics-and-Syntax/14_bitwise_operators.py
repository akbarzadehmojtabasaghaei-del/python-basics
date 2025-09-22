# ===================================================================================
# Chapter 13: A Deep Dive into Bitwise Operators
#
# This guide provides a comprehensive look at bitwise operators in Python. These
# operators manipulate integers on the level of their individual bits, which is
# essential for low-level programming, performance optimization, and specific
# algorithms like in cryptography and networking.
#
# Author:         Mojtaba Akbarzadeh Saghaei
# GitHub Profile: https://github.com/akbarzadehmojtabasaghaei-del/python-basics
# Last Updated:   2025-09-22
# ===================================================================================

# Let's define our numbers for the examples
a = 5  # Binary: 0b101
b = 6  # Binary: 0b110

# ===================================================================================
# ## Level 1: Core Bitwise Logic (AND, OR, XOR)
# These operators compare the bits of two numbers one by one.
# ===================================================================================

# --- Topic: `&` (Bitwise AND) ---
# Compares each bit. If *both* bits in the same position are 1, the result is 1. Otherwise, it's 0.
#   101  (5)
# & 110  (6)
# -----
#   100  (4)
result_and = a & b
print(f"a & b ({bin(a)} & {bin(b)}) = {result_and} ({bin(result_and)})") # -> 4

# --- Topic: `|` (Bitwise OR) ---
# Compares each bit. If *at least one* of the bits is 1, the result is 1. Otherwise, it's 0.
#   101  (5)
# | 110  (6)
# -----
#   111  (7)
result_or = a | b
print(f"a | b ({bin(a)} | {bin(b)}) = {result_or} ({bin(result_or)})") # -> 7

# --- Topic: `^` (Bitwise XOR - Exclusive OR) ---
# Compares each bit. If the bits are *different* (one is 1 and the other is 0), the result is 1. Otherwise, it's 0.
#   101  (5)
# ^ 110  (6)
# -----
#   011  (3)
result_xor = a ^ b
print(f"a ^ b ({bin(a)} ^ {bin(b)}) = {result_xor} ({bin(result_xor)})") # -> 3

# ===================================================================================
# ## Level 2: Unary and Shift Operators (NOT, <<, >>)
# These operators work on a single number's bits.
# ===================================================================================

# --- Topic: `~` (Bitwise NOT) ---
# Inverts all the bits of a number (0 becomes 1, and 1 becomes 0).
# The formula is `~x = -x - 1`. So, `~5` is `-5 - 1 = -6`.
# This is due to how negative numbers are stored (Two's Complement).
result_not = ~a
print(f"~a (~{bin(a)}) = {result_not}") # -> -6

# --- Topic: `<<` (Zero Fill Left Shift) ---
# Shifts the bits of a number to the left by a specified number of places.
# For each shift to the left, the number is multiplied by 2.
# 5 (0b101) shifted left by 2 becomes 0b10100 (which is 20).
result_left_shift = a << 2
print(f"a << 2 ({bin(a)} << 2) = {result_left_shift} ({bin(result_left_shift)})") # -> 20

# --- Topic: `>>` (Signed Right Shift) ---
# Shifts the bits of a number to the right by a specified number of places.
# For each shift to the right, the number is divided by 2 (floor division).
# 5 (0b101) shifted right by 2 becomes 0b1 (which is 1).
result_right_shift = a >> 2
print(f"a >> 2 ({bin(a)} >> 2) = {result_right_shift} ({bin(result_right_shift)})") # -> 1

# ===================================================================================
# ## Level 3: Practical Exercises and Use Cases
# Let's try some more examples to solidify the concepts.
# ===================================================================================

# --- Exercise 1: Checking if a number is Even or Odd ---
# A number is even if its last bit is 0, and odd if its last bit is 1.
# Using `& 1` is a very fast way to check this.
number = 14 # 0b1110
if (number & 1) == 0:
    print(f"\n{number} is Even.")
else:
    print(f"\n{number} is Odd.")

# --- Exercise 2: Swapping two numbers without a temp variable ---
x = 10 # 0b1010
y = 20 # 0b10100
print(f"Before swap: x={x}, y={y}")
x = x ^ y
y = y ^ x
x = x ^ y
print(f"After swap: x={x}, y={y}")

# --- Exercise 3: Permissions Management ---
# A common use case for setting flags.
READ_PERMISSION = 4    # 0b100
WRITE_PERMISSION = 2   # 0b010
EXECUTE_PERMISSION = 1 # 0b001

# Give a user read and execute permissions.
user_permissions = READ_PERMISSION | EXECUTE_PERMISSION # 0b100 | 0b001 -> 0b101 (5)
print(f"User permissions value: {user_permissions}")

# Now, check if the user has write permission.
# We use `&` to see if the "write" bit is on.
has_write = (user_permissions & WRITE_PERMISSION) > 0
print(f"Does the user have write permission? {has_write}") # -> False

# Now, check if the user has read permission.
has_read = (user_permissions & READ_PERMISSION) > 0
print(f"Does the user have read permission? {has_read}") # -> True


print("\n--- Bitwise Operators Mastery Guide: Complete ---")