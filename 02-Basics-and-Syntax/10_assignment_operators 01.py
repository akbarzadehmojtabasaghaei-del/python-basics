# ===================================================================================
# Chapter 6: Advanced Assignment Techniques
#
# This guide covers Pythonic ways of assigning values, including unpacking and
# the elegant one-line variable swap. It also introduces how to delete
# variable references using the `del` keyword.
#
# Author:         Mojtaba Akbarzadeh Saghaei
# GitHub Profile: https://github.com/akbarzadehmojtabasaghaei-del/python-basics
# LinkedIn:       www.linkedin.com/in/mojtaba-akbarzadeh-saghaei
# Last Updated:   2025-09-20
# ===================================================================================


# ===================================================================================
# ## Level 1: Unpacking Assignments
# Assigning items from a sequence (like a list or tuple) to multiple variables.
# ===================================================================================

# --- Topic: Unpacking a List ---
# You can extract values from a list directly into variables.
# The number of variables on the left must match the number of items on the right.

server_config = ["192.168.1.1", 8080, "admin"]
ip, port, username = server_config

print(f"Connecting to {ip} on port {port} as {username}.")

# WRONG: Number of variables does not match the number of items.
# ip, port = server_config # This will raise a ValueError.


# ===================================================================================
# ## Level 2: The Pythonic Variable Swap
# The most elegant way to swap the values of two variables.
# ===================================================================================

# --- Topic: Swapping Variables in One Line ---
# This is a classic Python idiom that showcases the power of tuple packing/unpacking.

# Your excellent practice code:
a = 1
b = 2
print(f"Before swap: a = {a}, b = {b}")

# How it works:
# 1. Right side (b, a) creates a temporary tuple in memory: (2, 1)
# 2. Left side (a, b) unpacks the values from that tuple.
#    - `a` gets the first item (2).
#    - `b` gets the second item (1).
a, b = b, a

print(f"After swap: a = {a}, b = {b}")
print(f"ID of 'a' after swap: {id(a)}")
print(f"ID of 'b' after swap: {id(b)}")


# ===================================================================================
# ## Level 3: Deleting Variable Names
# How to remove a variable reference from memory.
# ===================================================================================

# --- Topic: The `del` Keyword ---
# The `del` keyword is used to remove a name (variable) from the current scope.
# It doesn't necessarily delete the object, just the reference to it.

user_session_id = "xyz-123-abc"
print(f"Session ID exists: {user_session_id}")

# Now, we delete the variable name.
del user_session_id

# Trying to access it now will cause an error because the name is no longer defined.
# WRONG:
# print(user_session_id) # This will raise a NameError.

# CORRECT: Check if the variable exists before using it (more advanced concept).
if 'user_session_id' in locals():
    print("Session ID is still available.")
else:
    print("Session ID has been deleted successfully.")


print("\n--- Advanced Assignment Mastery Guide: Complete ---")

