"""Arrays are collections of a finite number of homogeneous elements, each identified by an index or key."""
# বাংলা : অ্যারে হল একটি সীমিত সংখ্যক সমান উপাদানের সংগ্রহ, প্রতিটি উপাদান একটি সূচক বা কী দ্বারা চিহ্নিত।

# Array in Python programming
import sys

arr = [1, 2, 3, 4, 5]
print(arr)  # Output: [1, 2, 3, 4, 5]

# Accessing Array Elements
print(arr[0])  # Output: 1

# Change Array Elements
arr[0] = 10

# Loop Through an Array
for x in arr:
    print(x)

# Array Length
print(len(arr))  # Output: 5

# Add Array Elements
arr.append(6)

# Remove Array Elements
arr.pop(0)

# Array Methods

# sort() : sort method sorts the list ascending by default.
arr.sort()
print("Sorted Array: ", arr)  # Output: [2, 3, 4, 5, 6]

# reverse() : reverse method reverses the list.
arr.reverse()
print("Reversed Array: ", arr)  # Output: [6, 5, 4, 3, 2]

# copy() : copy method returns a copy of the specified list.
new_array = arr.copy()
print("Copied Array: ", new_array)  # Output: [6, 5, 4, 3, 2]

# count() : count method returns the number of elements with the specified value.
count = arr.count(3)
print("Counted Array for value 3: ", count)  # Output: 1

# index() : index method returns the index of the first element with the specified value.
print("Index of 3: ", arr.index(3))  # Output: 3

# insert() : insert method adds an element at the specified position.
arr.insert(0, 0)
print("Inserted Array: ", arr)  # Output: [0, 1, 2, 3, 4, 5]

# remove() : remove method removes the first occurrence of the element with the specified value.
arr.remove(6)
print("Removed value 6 from Array: ", arr)  # Output: [0, 1, 2, 3, 4, 5]

# extend() : extend method adds the specified list elements (or any iterable) to the end of the current list.
arr.extend([6, 7, 8])
print("Extended Array: ", arr)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# clear() : clear method removes all the elements from the list.
arr.clear()
print("Cleared Array: ", arr)

# array slicing : array slicing is the process of taking a subset of elements from an array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# arr[start:end] : slicing from index number 2 and end before index number 5
print(arr[2:5])  # Output: [3, 4, 5]

# arr[:end] : slicing from the beginning to before index number 5
print(arr[:5])  # Output: [1, 2, 3, 4, 5]

# arr[start:] : slicing from index number 5 to the end
print(arr[5:])  # Output: [6, 7, 8, 9]

# arr[-3:-1] : negative indexing slicing.
# It means slicing from the 3rd element from the end to the before 1st element from the end
print(arr[-3:-1])  # Output: [7, 8]

# arr[1:7:2] : slicing from index number 1 to before index number 7 with a step of 2
print(arr[1:7:2])  # Output: [2, 4, 6] # start, end, step

memory_size = sys.getsizeof(arr[0])
print(f"Memory size of the array element: {memory_size} bytes")

memory_size = sys.getsizeof(arr)
print(f"Memory size of the array: {memory_size} bytes")
