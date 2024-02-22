"""Linked List implementation in Python."""


# A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
# The elements in a linked list are linked using pointers.

# Advantages of Linked List:
# 1. Dynamic Data Structure: A linked list is a dynamic data structure so it can grow and shrink at runtime by allocating and deallocating memory.
# 2. Insertion and Deletion: Insertion and deletion of a node are really easier. Unlike an array here we don’t have to shift elements after insertion or deletion of an element.
# 3. No Memory Wastage: In case of an array, there is a lot of memory wastage as the size of the array is fixed, but in a linked list, there is no memory wastage.

# Disadvantages of Linked List:
# 1. Memory Usage: More memory is required as compared to arrays because of the storage used by pointers.
# 2. Traversal: In linked list, the traversal is more time-consuming because the linked list is not stored in contiguous memory locations.
# 3. Reverse Traversal: In a singly linked list, it is not possible to traverse the list in the reverse direction.

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            suffix = ' --> '
            if itr.next is None:
                llstr += f"{str(itr.data)} [None]"
                break
            else:
                llstr += f"{str(itr.data)}, [{str(itr.next)}]" + suffix
            itr = itr.next
        print(llstr)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_beginning(12)
    ll.print()
