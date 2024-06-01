"""
    Recursion is a function that calls itself.
    It is a way of solving problems by breaking them down into smaller and simpler problems.
"""
# Recursion not good when it comes to space complexity,


# Sum of 5 natural numbers using recursion
def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)


print(sum_of_natural_numbers(5))  # Output: 15


# explaining the above code, step by step and how it works.
# 1. sum_of_natural_numbers(5) = 5 + sum_of_natural_numbers(4)
# 2. sum_of_natural_numbers(4) = 4 + sum_of_natural_numbers(3)
# 3. sum_of_natural_numbers(3) = 3 + sum_of_natural_numbers(2)
# 4. sum_of_natural_numbers(2) = 2 + sum_of_natural_numbers(1)
# 5. sum_of_natural_numbers(1) = 1

# 5 + sum_of_natural_numbers(4)
# 5 + 4 + sum_of_natural_numbers(3)
# 5 + 4 + 3 + sum_of_natural_numbers(2)
# 5 + 4 + 3 + 2 + sum_of_natural_numbers(1)
# 5 + 4 + 3 + 2 + 1

# 5 + 4 + 3 + 2 + 1 = 15



