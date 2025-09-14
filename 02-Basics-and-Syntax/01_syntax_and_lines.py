# ===================================================================================
# Chapter 2: Python Syntax - A Deep Dive Mastery Guide
#
# This file is a comprehensive, personalized guide to Python's syntax, created as
# part of a professional development journey. It covers concepts from the absolute
# fundamentals to advanced, professional-grade structures.
#
# Author:         Mojtaba Akbarzadeh Saghaei
# GitHub Profile: https://github.com/akbarzadehmojtabasaghaei-del/python-basics
# LinkedIn:       www.linkedin.com/in/mojtaba-akbarzadeh-saghaei
# Last Updated:   2025-09-14
# ===================================================================================


# ===================================================================================
# ## Level 1: The Building Blocks
# These are the absolute fundamentals of the Python language.
# ===================================================================================

# --- Topic: Keywords ---
# Keywords are reserved words that have special meaning. You cannot use them as names.

# WRONG: Using a keyword as a variable name.
# def = "My Function"  # This will raise a SyntaxError.

# CORRECT: Using a valid identifier.
function_name = "calculate_average"
print(f"Correct identifier: {function_name}")


# --- Topic: Identifiers (Variable Names) ---
# Identifiers are the names you give to variables, functions, etc.
# Python is case-sensitive.

# WRONG: Using a variable with the wrong case.
my_name = "Mojtaba"
# print(My_Name)  # This will raise a NameError because 'My_Name' is not defined.

# CORRECT: Using the exact same case.
print(f"User's name is: {my_name}")


# ===================================================================================
# ## Level 2: Structural Rules
# This is where Python's unique and famous syntax comes into play.
# ===================================================================================

# --- Topic: Indentation ---
# THIS IS THE MOST IMPORTANT RULE IN PYTHON. It defines code blocks.

# WRONG: Missing indentation after a block statement.
user_role = "admin"
# if user_role == "admin":
# print("Access granted.") # This will raise an IndentationError.

# CORRECT: Using 4 spaces for indentation inside a block.
if user_role == "admin":
    print("User is an admin.")
    print("Full access granted.")


# --- Topic: Statements and Lines (Physical vs. Logical Lines) ---
# A physical line is what you see. A logical line is a complete command.
# You can split one logical line across multiple physical lines for readability.

# Method 1 (Implicit Joining - PREFERRED): Use parentheses (), brackets [], or braces {}.
my_github_projects = [
    "Project Alpha: AI Chatbot",
    "Project Beta: Security Scanner",
    "Project Gamma: Data Analysis Dashboard"
]

# Method 2 (Explicit Joining): Use a backslash \.
total_score = 100 + 200 + 300 + \
              400 + 500
print(f"Total score is: {total_score}")


# --- Topic: Comments vs. Docstrings ---
# Comments are for developers. Docstrings are for documentation.

# This is a comment. I'm checking if the user is authenticated.
is_authenticated = True

def connect_to_database(db_name: str):
    """
    This is a Docstring. It explains WHAT the function does.
    It can be accessed by tools like help().

    Args:
        db_name (str): The name of the database to connect to.
    """
    print(f"Connecting to database: {db_name}")


# ===================================================================================
# ## Level 3: Intermediate Syntax (The Pythonic Way)
# Writing code like a professional Python developer.
# ===================================================================================

# --- Topic: List Comprehensions ---
# A concise and readable way to create lists.

# Example 1: Squaring numbers (from before)
squares = [n * n for n in range(1, 6)] # Result: [1, 4, 9, 16, 25]

# Example 2: Creating a list of usernames from a list of dictionaries
users = [{"name": "Alice", "role": "dev"}, {"name": "Bob", "role": "admin"}]
usernames = [user["name"] for user in users] # Result: ['Alice', 'Bob']
print(f"Usernames found: {usernames}")


# --- Topic: The Walrus Operator (:=) ---
# Assigns a value to a variable as part of a larger expression.

# Example 1: Simple length check (from before)
data = ["a", "b", "c"]
if (n := len(data)) > 2:
    print(f"Data contains {n} items.")

# Example 2: A simple loop that asks for input until user types 'quit'.
# while (command := input("Enter command (or 'quit' to exit): ")) != "quit":
#     print(f"Executing command: {command}")


# --- Topic: Advanced Unpacking ---
# Using the star operator (*) to capture multiple items from a list.

# Example 1: First, middle, last (from before)
scores = [98, 95, 88, 84, 72]
highest, *middle_scores, lowest = scores
print(f"Highest: {highest}, Middle: {middle_scores}, Lowest: {lowest}")

# Example 2: In a function call
def calculate_sum(a, b, c):
    return a + b + c

my_numbers = [10, 20, 30]
print(f"Sum is: {calculate_sum(*my_numbers)}") # Unpacks the list into arguments a, b, c


# ===================================================================================
# ## Level 4: Advanced & Abstract Syntax
# Syntax for building powerful, reusable, and robust software.
# ===================================================================================

# --- Topic: Decorators (@) ---
# A function that takes another function and extends its behavior.

def admin_only(func):
    """A decorator to check if the user has admin rights."""
    def wrapper():
        # In a real app, you would check a real user's role
        if user_role == "admin":
            print("Admin access confirmed.")
            func()
        else:
            print("Access denied. Admin rights required.")
    return wrapper

@admin_only
def delete_critical_data():
    """A sensitive function that should only be run by admins."""
    print("Critical data has been deleted.")

delete_critical_data()


# --- Topic: Context Managers (with statement) ---
# Manages resources by guaranteeing that setup and teardown phases are executed.

# Example 1: File handling (from before)
with open("my_log_file.txt", "w") as f:
    f.write(f"Log entry for user: {my_name}\n")
    f.write("Operation successful.")
# The file is automatically and safely closed here.

# Example 2: Managing a database connection (conceptual)
# with database_connection("my_db") as db:
#     db.execute_query("SELECT * FROM users")
# The connection is automatically closed even if errors occur inside the block.


# --- Topic: Type Hints ---
# A way to statically indicate the type of a variable for clarity and error-checking.

def get_profile_info(user_id: int) -> dict:
    """Fetches user profile information from a database."""
    # Imagine this connects to a database and gets data
    if user_id == 1:
        return {"name": "Mojtaba Akbarzadeh Saghaei", "role": "AI & Security Student"}
    return {}

my_profile = get_profile_info(1)
print(f"Profile fetched: {my_profile}")

# A static analysis tool could warn you if you tried: get_profile_info("some_string")


print("\n--- Python Syntax Mastery Guide: Complete ---")