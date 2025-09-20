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
print("\n--- Using the end Parameter ---")
print("Processing file:", end=" ")
print("80%", end="...")
print("Done.")


# ===================================================================================
# ## Level 3: Professional Printing Techniques
# Combining parameters for advanced and practical use cases.
# ===================================================================================

# --- Topic: Combining `sep` and `end` ---
print("\n--- Combining sep and end ---")
print("Permissions", "user", "group", "others", sep=":", end="\n\n")
print("read", "write", "execute", sep="-")


# --- Topic: A Note on F-Strings vs. print() Parameters ---
user = "Mojtaba"
score = 95
print(f"User '{user}' scored {score}", end=" | Status: OK\n")


# ===================================================================================
# ## Level 4: Exploring Edge Cases (Your Practice Section)
# Exploring less common but insightful behaviors of the print() function.
# ===================================================================================

# --- Topic: Using Newline Characters (`\n`) as Arguments ---
# You practiced passing the newline character `\n` directly as an argument.
# Let's analyze what happens.

print("\n--- Exploring `\n` as an argument ---")
print(5, '\n', 9, '\n')
# BEHAVIOR: `print` treats `\n` like any other string. It prints the argument, then the
# separator. When it prints the `\n` string, the cursor moves to a new line.

# --- Your practice with different separators ---
print("--- Using `\n` as an argument with custom `sep` ---")
print(x, '\n', '\n', 5, 9, '\n', sep=';')
print(5, 6, '\n', 9, '\n', sep='hi')
print(78, 78, '\n', 78, 78, sep='/')

# PROFESSIONAL ADVICE:
# While this works, it can make the code's intent less clear. For creating multi-line
# output, using multiple print() calls or f-strings is often more readable.

# More readable alternative for the same visual output:
print("\n--- More readable multi-line printing ---")
print(5)
print(9)
print() # Prints an empty line

# Or using a single f-string:
print(f"Here is one number: {5}\nAnd here is another: {9}\n")
print("\n--- print() Function Mastery Guide: Complete ---")