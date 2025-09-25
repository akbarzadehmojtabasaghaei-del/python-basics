# ===================================================================================
# Chapter 12: Identity Operators (is, is not)
#
# This guide revisits the crucial concept of identity vs. equality. Identity
# operators compare the memory location of two objects, not just their value.
#
# Author:         Mojtaba Akbarzadeh Saghaei
# GitHub Profile: https://github.com/akbarzadehmojtabasaghaei-del/python-basics
# LinkedIn:       https://www.linkedin.com/in/mojtaba-akbarzadeh-saghaei

# ===================================================================================

# --- Topic: `is` vs `==` Revisited ---
# `==` checks if the VALUES are the same.
# `is` checks if they are the EXACT SAME OBJECT in memory.

# For small integers, Python often reuses the same object.
z = 10
e = 10
print(f"z == e -> {z == e}") # True (Values are the same)
print(f"z is e -> {z is e}") # True (Python reuses the object for the integer 10)

# For mutable objects like lists, it's a different story.
c = [1, 2]
v = [1, 2]
print(f"\nc == v -> {c == v}") # True (The lists contain the same values)
print(f"c is v -> {c is v}") # False (They are two separate list objects in memory)
print(f"ID of c: {id(c)}, ID of v: {id(v)}")

# --- Topic: The `is not` Operator ---
# Returns `True` if two variables do *not* point to the same object.
m = [1, 3, 5]
print(f"\nc is not m -> {c is not m}") # True (They are different objects)
print(f"c is not c -> {c is not c}") # False (c IS itself)

print("\n--- Identity Operators Mastery Guide: Complete ---")