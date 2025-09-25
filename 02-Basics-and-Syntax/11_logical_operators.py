# ===================================================================================
# Chapter 11: Membership Operators (in, not in)
#
# This guide covers the membership operators, which are used to test if a
# sequence (like a string, list, or tuple) contains a specific value.
#
# Author:         Mojtaba Akbarzadeh Saghaei
# GitHub Profile: https://github.com/akbarzadehmojtabasaghaei-del/python-basics
# ===================================================================================

s = "hi my name is 12"
l = [1, 2, 3, 'rz']

# --- Topic: The `in` Operator ---
# Returns `True` if a value is found in the sequence.
print(f"'n' in s -> {'n' in s}")   # True
print(f"'1' in s -> {'1' in s}")   # True (searches for the character '1')
print(f"1 in l -> {1 in l}")     # True (searches for the number 1)

# --- Topic: The `not in` Operator ---
# Returns `True` if a value is *not* found in the sequence.
print(f"'12' not in s -> {'12' not in s}") # False, because '12' IS in s.
print(f"'@' not in s -> {'@' not in s}")   # True

# --- Topic: Common Misconceptions ---
# 1. Type matters: Searching for the number `1` is different from the character `'1'`.
# print(1 in s) # This would raise a TypeError because `in` on a string expects a string.

# 2. Checking for multiple items.
# Your discovery: `1, 2, 3 in l`
# This evaluates as `(1, 2, (3 in l))` which becomes `(1, 2, True)`.
# To check if multiple items are in a list, you need a different approach.
# A more advanced way using sets:
print(f"Are 1, 2, and 3 all in l? { {1, 2, 3}.issubset(l) }") # True

print("\n--- Membership Operators Mastery Guide: Complete ---")