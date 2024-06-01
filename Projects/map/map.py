"""
    what is the map function?
    - The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
"""

marks = [80, 90, 85, 70, 95]


def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


# grades = map(grade, marks)
# print("marks: ", marks)
# print("grades: ", next(grades))
# print("grades: ", next(grades))

# another way to use map function
grades = list(map(grade, marks))
print("marks: ", marks)
print("grades: ", grades)
