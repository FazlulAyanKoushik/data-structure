"""
    What is a filter?
    A filter is a function that takes an iterable and returns another iterable.
"""

marks = [40, 90, 85, 70, 55]


def is_pass(marks):
    return marks >= 70


pass_marks = filter(is_pass, marks)

print("marks: ", marks)
print("pass_marks: ", list(pass_marks))
