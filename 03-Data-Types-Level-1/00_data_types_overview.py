# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Chapter 16: Python's Core Data Types
#
# This guide provides a comprehensive overview of the fundamental data types
# in Python. Understanding each type's purpose and behavior is essential for
# storing and manipulating data effectively.
#
# Author:         Mojtaba Akbarzadeh Saghaei
# GitHub Profile: https://github.com/akbarzadehmojtabasaghaei-del/python-basics
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# ===================================================================================
# ## Level 1: Single Value Types
# These types hold a single piece of data.
# ===================================================================================

# --- Topic: Numeric Types (int, float, complex) ---
# For handling numbers.
integer_num = 5         # int: For whole numbers.
float_num = 8.5         # float: For numbers with a decimal point.
complex_num = 5 + 6j    # complex: For complex numbers (common in scientific computing).

print(f"Type of {integer_num} is: {type(integer_num)}")
print(f"Type of {float_num} is: {type(float_num)}")
print(f"Type of {complex_num} is: {type(complex_num)}")

# --- Topic: Boolean Type (bool) ---
# For representing truth values. It can only be `True` or `False`.
is_active = True
has_permission = False
print(f"\nType of {is_active} is: {type(is_active)}")

# --- Topic: The None Type (NoneType) ---
# A special type that represents the absence of a value.
# It's often used as a placeholder.
user_email = None
print(f"Type of user_email is: {type(user_email)}")


# ===================================================================================
# ## Level 2: Sequence Types (Ordered Collections)
# These types store an ordered sequence of items.
# ===================================================================================

# --- Topic: String (str) ---
# An ordered, *immutable* sequence of characters. Immutable means it cannot be changed after creation.
my_string = "hi my name"
print(f"\nType of '{my_string}' is: {type(my_string)}")
# You can access parts of a string using slicing.
print(f"Slice of my_string [2:5] is: '{my_string[2:5]}'") # -> ' my'

# --- Topic: List (list) ---
# An ordered, *mutable* collection of items. Mutable means you can change, add, or remove items.
my_list = [1, 2, 3, 'rz', True]
print(f"Type of {my_list} is: {type(my_list)}")

# --- Topic: Tuple (tuple) ---
# An ordered, *immutable* collection of items. Like a list, but cannot be changed.
# They are generally faster than lists.
my_tuple = (1, 2, 3, 5, 5, 5, 6, 4)
print(f"Type of {my_tuple} is: {type(my_tuple)}")
# Slicing works on tuples too.
print(f"Slice of my_tuple [2:4] is: {my_tuple[2:4]}") # -> (3, 5)


# ===================================================================================
# ## Level 3: Unordered & Key-Value Collections
# These types store collections of items without a specific order.
# ===================================================================================

# --- Topic: Set (set) ---
# An *unordered* collection of *unique* items.
# Notice how the duplicate `5`s are automatically removed.
my_set = {1, 2, 3, 5, 5, 5, 6, 4}
print(f"\nMy set automatically handles duplicates: {my_set}")
print(f"Type of {my_set} is: {type(my_set)}")
# Because sets are unordered, you cannot access items by index or slice them.
# my_set[0] -> This would cause a TypeError.

# --- Topic: Dictionary (dict) ---
# An *unordered* collection of `key:value` pairs.
# Used to store related data in a structured way.
my_dict = {"mojtaba": "handsome", "user_id": 12, "is_admin": False}
print(f"My dictionary: {my_dict}")
print(f"Type of {my_dict} is: {type(my_dict)}")


print("\n--- Core Data Types Mastery Guide: Complete ---")