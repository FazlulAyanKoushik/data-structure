"""
    Recursion is a function that calls itself.
    It is a way of solving problems by breaking them down into smaller and simpler problems.
"""
# Recursion not good when it comes to space complexity,


# How check a number is power of 2 using recursion
def is_power_of_two(n):
    if n == 1:
        return True
    elif n % 2 != 0 or n == 0:
        return False
    else:
        return is_power_of_two(n / 2)


print(is_power_of_two(12))  # Output: True


# How check a number is power of 4 using recursion
def is_power_of_four(n):
    if n == 1:
        return True
    elif n % 4 != 0 or n == 0:
        return False
    else:
        return is_power_of_four(n / 4)


print(is_power_of_four(16))  # Output: True
