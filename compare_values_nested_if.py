# PROGRAMMER:   Marlena Fabrick
# PROGRAM NAME: Comparing Two Values — Nested IF Statements
# DATE WRITTEN: 9/21/2020
# UPDATED:      2026 — removed unused toFixed import, fixed indentation
#                      in the nested else block, added input validation
#
# PURPOSE: Compare two numeric values entered by the user and report whether
#          they are equal, or which one is greater. Uses NESTED IF statements:
#          a single outer if/else with a second if/else inside the else branch.
#
# KEY CONCEPT — NESTED IF:
#   if value1 == value2:       ← outer if
#       (equal)
#   else:
#       if value1 < value2:    ← inner if (nested inside else)
#           (less than)
#       else:
#           (greater than)     ← inner else
#
# Compare this to compare_values_sequential_if.py, which uses three
# separate (sequential) if statements instead.

# ============================================================
# Declare all variables in alphabetical order
# INPUT OPERATIONS — collect two numeric values from the user

# Loop until valid numeric input is provided for value 1
while True:
    try:
        print("Enter the first value: ")
        value1 = float(input())
        break  # Exit loop once valid input is received
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Loop until valid numeric input is provided for value 2
while True:
    try:
        print("Enter the second value: ")
        value2 = float(input())
        break  # Exit loop once valid input is received
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# OUTPUT LINE FOR SEPARATION OF OUTPUT
print("=" * 75)

# ============================================================
# NESTED IF STATEMENTS TO COMPARE TWO VALUES

if value1 == value2:
    # The two values are equal — report equality
    print("VALUE #1 ---> " + format(value1, " ,.2f") +
          " and VALUE #2 ---> " + format(value2, " ,.2f") + " are equal.")
else:
    # The values are NOT equal — check which is smaller
    if value1 < value2:
        # Value 1 is the smaller of the two
        print("VALUE #1 ---> " + format(value1, " ,.2f") +
              " is less than VALUE #2 ---> " + format(value2, " ,.2f") + ".")
    else:
        # Value 1 is the larger of the two (inner else — end of nested if)
        print("VALUE #1 ---> " + format(value1, " ,.2f") +
              " is greater than VALUE #2 ---> " + format(value2, " ,.2f") + ".")
    # end nested if statement

# OUTPUT LINE FOR SEPARATION OF OUTPUT
print("=" * 75)

# END PROGRAM
```

