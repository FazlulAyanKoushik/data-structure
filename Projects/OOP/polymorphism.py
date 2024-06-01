"""
    Polymorphism is the ability to define a generic interface that can be used to refer to objects of different classes,
    and it can be achieved in Python through method overloading and method overriding.
"""

# Polymorphism means same function name (but different signatures) being uses for different
# types. This allows objects to be passed around without knowing the details of the object.

# Example of Polymorphism
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5
my_string = "Hello, World!"
print(len(my_string))  # Output: 13

# In the above example, the len() function is used to find the length of a list and a string. The len() function is
# polymorphic because it can be used with different types of objects.


"""
    Method overloading is the ability to define multiple methods with the same name but with different parameters.
"""


# Example of Method Overloading
class PythonOOP:
    def displayInfo(self, name="") -> None:
        print("Welcome to Python OOP Tutorial! " + name)


python_oop = PythonOOP()
python_oop.displayInfo()  # Output: Welcome to Python OOP Tutorial!

python_oop.displayInfo("John")  # Output: Welcome to Python OOP Tutorial! John
# In the above example, the displayInfo() method is overloaded with two different signatures.
# The first method does not take any parameters, and the second method takes one parameter.
# This is an example of method overloading in Python.


"""
    Method overriding is the ability to define a method in the subclass that is already defined in the superclass.
"""


# Example of Method Overriding
class Animal(PythonOOP):
    def displayInfo(self, name="") -> None:
        super().displayInfo()  # Call the displayInfo() method of the superclass
        print("Welcome to Animal World! " + name)


animal = Animal()
animal.displayInfo()  # Output: Welcome to Animal World!

# In the above example, the displayInfo() method is overridden in the Animal class, which is a subclass of the PythonOOP
