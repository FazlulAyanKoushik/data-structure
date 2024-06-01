from collections import deque

# Declaring deque
queue = deque(['name', 'age', 'DOB', 'Soap', 'address'])

print(queue)

# Adding elements to the right
queue.append('right')

# Adding elements to the left
queue.appendleft('left')

print(queue)

# Removing elements from the right
queue.pop()
print("After removing from the right: ", queue)

# Removing elements from the left
queue.popleft()
print("After removing from the left: ", queue)

# Reversing the queue
queue.reverse()

print("After reversing: ", queue)

# Rotating the queue
queue.rotate(2)
print("After rotating: ", queue)

