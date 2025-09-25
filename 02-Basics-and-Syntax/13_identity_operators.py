# ===================================================================================
# Chapter 5: Identity, Memory, and `is` vs `==`
#
# This guide explores the advanced concepts of object identity and memory
# management in Python. Understanding the difference between checking for
# equality (`==`) and identity (`is`) is critical for writing robust code.
#
# Author:         Mojtaba Akbarzadeh Saghaei
# GitHub Profile: https://github.com/akbarzadehmojtabasaghaei-del/python-basics
# LinkedIn:       www.linkedin.com/in/mojtaba-akbarzadeh-saghaei
# ===================================================================================


# ===================================================================================
# ## Level 1: Understanding Object Identity with id()
# Every object in Python has a unique ID, which represents its memory address.
# ===================================================================================

# --- Topic: The `id()` Function ---
# `id()` returns the unique identity (a memory address) of an object.
# This allows us to see if two variables refer to the *exact same object*.

# Your excellent practice code:
x = 2
print(f"Object '2' is at memory address: {id(x)}")

x = 3
print(f"Object '3' is at memory address: {id(x)}")

# Python is efficient: for small integers, it reuses existing objects.
b = 2
print(f"Variable 'b' also points to address: {id(b)}") # Should be same as first `id(x)`

# Assignment makes variables point to the same object.
b = x # 'b' now points to the same object as 'x' (which is the object '3').
print(f"Now id(x) is {id(x)} and id(b) is {id(b)}. They are the same.")


# --- Topic: Multiple Assignment and Identity ---
# Chained assignment makes all variables point to the right-most object.
z = b = x # All three variables now point to the object '3'.
print(f"After z=b=x -> id(x): {id(x)}, id(b): {id(b)}, id(z): {id(z)}")


# ===================================================================================
# ## Level 2: Identity Operator (`is`) vs. Equality Operator (`==`)
# This is a classic interview question and a crucial concept.
# ===================================================================================

# --- Topic: The Equality Operator (`==`) ---
# `==` checks if the **values** of two variables are equal.

a = [1, 2, 3]
b = [1, 2, 3]

# The lists have the same content, so their values are equal.
print(f"\nAre the values of a and b equal? (a == b) -> {a == b}") # This will be True.


# --- Topic: The Identity Operator (`is`) ---
# `is` checks if two variables point to the **exact same object** in memory.
# In other words, it checks if their `id()` is the same.

# Although `a` and `b` have the same value, they are two separate list objects
# created in different memory locations.
print(f"Are a and b the same object? (a is b) -> {a is b}") # This will be False.
print(f"id(a) is {id(a)}, but id(b) is {id(b)}")


# --- Let's make them the same object ---
c = a  # `c` is now just another label for the *same object* that `a` points to.
print(f"Are a and c the same object? (a is c) -> {a is c}") # This will be True.


# PROFESSIONAL ADVICE:
# - Use `==` when you care about the *value* of an object (99% of the time).
# - Use `is` only when you specifically need to check if two variables are the
#   *exact same instance*. This is most common when checking against `None`.

# The Pythonic way to check if a variable is None:
my_variable = None
if my_variable is None:
    print("The variable is not set.")

# WRONG (but works): if my_variable == None:
# RIGHT (Pythonic):  if my_variable is None:


print("\n--- Identity and Memory Mastery Guide: Complete ---")