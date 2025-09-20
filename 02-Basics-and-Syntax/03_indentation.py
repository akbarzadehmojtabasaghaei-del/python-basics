# ===================================================================================
# Chapter 3: Mastering the print() Function
#
# This guide explores the advanced capabilities of Python's built-in print()
# function. Understanding parameters like `sep` and `end` is crucial for
# creating clean, readable, and well-formatted console output.
#
# Author:         Mojtaba Akbarzadeh Saghaei
# GitHub Profile: https://github.com/akbarzadehmojtabasaghaei-del/python-basics
# LinkedIn:       www.linkedin.com/in/mojtaba-akbarzadeh-saghaei
# Last Updated:   2025-09-20
# ===================================================================================


# ===================================================================================
# ## Level 1: Default Print Behavior
# How print() works out-of-the-box.
# ===================================================================================

# By default, `print` separates arguments with a single space and ends with a newline.
print("Hello", "Python", "World")
print("This is a new line.")
# OUTPUT:
# Hello Python World
# This is a new line.


# ===================================================================================
# ## Level 2: Customizing Print Output
# Taking control of the output format with special parameters.
# ===================================================================================

# --- Topic: The `sep` Parameter ---
# The `sep` (separator) parameter controls the character(s) used to separate arguments.

# CORRECT: Using different separators to format data.
X = 2
x = 3
Y = 6
y = 12

print("--- Using Different Separators ---")
print(x, y, Y, X, sep=":")    # Use a colon
print(x, y, Y, X, sep=", ")   # Use a comma and a space for CSV-like output
print(x, y, Y, X, sep=" -> ") # Use an arrow to show a sequence


# --- Topic: The `end` Parameter ---
# The `end` parameter controls the character(s) printed at the very end of the line.

# WRONG: Thinking `end` separates items. It only affects the end of the print call.
# print("item1", "item2", end="---") # This prints "item1 item2---" not "item1---item2"

# CORRECT: Using `end` to print multiple statements on the same line.
print("Processing file:", end=" ")
# Imagine a time-consuming task happens here
print("80%", end="...")
# Imagine more work
print("Done.")


# ===================================================================================
# ## Level 3: Professional Printing Techniques
# Combining parameters for advanced and practical use cases.
# ===================================================================================

# --- Topic: Combining `sep` and `end` ---
# You can use both parameters in a single call for maximum control.

# Example: Generating a list of file permissions.
print("Permissions", "user", "group", "others", sep=":", end="\n\n")
# The double newline `\n\n` adds an extra blank line for spacing.
print("read", "write", "execute", sep="-")


# --- Topic: A Note on F-Strings vs. print() Parameters ---
# F-Strings are for formatting the *content* of a single string.
# `sep` and `end` are for controlling the *behavior* of the print function itself.
# They solve different problems but can be used together.

user = "Mojtaba"
score = 95
print(f"User '{user}' scored {score}", end=" | Status: OK\n")


print("\n--- print() Function Mastery Guide: Complete ---")