# ===================================================================================
# Chapter 9: Complete Guide to All Assignment Operators
#
# This guide provides a comprehensive overview of every assignment operator in
# Python, including arithmetic and the more advanced bitwise operators. Each
# operator is demonstrated with a practical example.
#
# Author:         Mojtaba Akbarzadeh Saghaei
# GitHub Profile: https://github.com/akbarzadehmojtabasaghaei-del/python-basics
# LinkedIn:       https://www.linkedin.com/in/mojtaba-akbarzadeh-saghaei
# ===================================================================================


# ===================================================================================
# ## Level 1: Arithmetic Augmented Assignment
# These are the most common operators, used for numerical calculations.
# ===================================================================================

# --- Topic: `+=` (Add and assign) ---
score = 100
score += 10  # score = score + 10
print(f"Score after `+=`: {score}")  # -> 110

# --- Topic: `-=` (Subtract and assign) ---
health = 100
health -= 25 # health = health - 25
print(f"Health after `-=`: {health}") # -> 75

# --- Topic: `*=` (Multiply and assign) ---
mana = 50
mana *= 1.5 # mana = mana * 1.5
print(f"Mana after `*=`: {mana}") # -> 75.0

# --- Topic: `/=` (True Divide and assign) ---
distance = 100
distance /= 2 # distance = distance / 2
print(f"Distance after `/=`: {distance}") # -> 50.0 (always a float)

# --- Topic: `//=` (Floor Divide and assign) ---
item_count = 25
item_count //= 10 # item_count = item_count // 10
print(f"Item stacks after `//=`: {item_count}") # -> 2

# --- Topic: `%=` (Modulo and assign) ---
time_left = 125
time_left %= 60 # time_left = time_left % 60 (calculates seconds left)
print(f"Seconds left after `%=`: {time_left}") # -> 5

# --- Topic: `**=` (Exponent and assign) ---
power_level = 2
power_level **= 3 # power_level = power_level ** 3
print(f"Power level after `**=`: {power_level}") # -> 8


# ===================================================================================
# ## Level 2: Bitwise Augmented Assignment
# These are advanced operators that work on the binary representation of numbers.
# ===================================================================================

# --- Topic: `&=` (Bitwise AND and assign) ---
# Used to check or clear specific bits.
# Example: `5` is `0101` in binary. `3` is `0011`. `5 & 3` is `0001` (which is 1).
permissions = 5  # Binary: 0101
mask = 3         # Binary: 0011
permissions &= mask
print(f"\nPermissions after `&=`: {permissions}") # -> 1

# --- Topic: `|=` (Bitwise OR and assign) ---
# Used to set specific bits.
# Example: `5 | 3` is `0111` (which is 7).
permissions = 5  # Binary: 0101
permissions |= 3 # Turn on the bits from the mask
print(f"Permissions after `|=`: {permissions}") # -> 7

# --- Topic: `^=` (Bitwise XOR and assign) ---
# Used to toggle bits (if a bit is 1, it becomes 0, and vice-versa).
# Example: `5 ^ 3` is `0110` (which is 6).
permissions = 5  # Binary: 0101
permissions ^= 3 # Toggle the bits
print(f"Permissions after `^=`: {permissions}") # -> 6

# --- Topic: `>>=` (Bitwise Right Shift and assign) ---
# Shifts bits to the right, effectively dividing by 2 for each shift.
# Example: `16` is `10000`. Shifting right by 2 (`>>= 2`) gives `100` (which is 4).
number = 16
number >>= 2
print(f"Number after `>>=`: {number}") # -> 4

# --- Topic: `<<=` (Bitwise Left Shift and assign) ---
# Shifts bits to the left, effectively multiplying by 2 for each shift.
# Example: `4` is `100`. Shifting left by 2 (`<<= 2`) gives `10000` (which is 16).
number = 4
number <<= 2
print(f"Number after `<<=`: {number}") # -> 16


print("\n--- Complete Guide to Assignment Operators: Done ---")