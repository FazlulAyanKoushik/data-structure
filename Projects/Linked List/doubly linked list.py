"""Doubly Linked list implementation in Python"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """This will add a new node to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            new_node.prev = last_node

    def prepend(self, data):
        """This will add a new node to the beginning of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_node(self, key):
        """This will delete a node from the list. If the node is the head, it will delete the head and make the next
        node the head. If the node is not the head, it will delete the node and connect the previous node to the next
        node."""
        current_node = self.head
        while current_node:
            if current_node.data == key and current_node == self.head:
                # Case 1: If the node to be deleted is the head node and there is only one node in the list.
                if not current_node.next:
                    current_node = None
                    self.head = None
                    return
                else:
                    # Case 2: If the node to be deleted is the head node and there are more than one node in the list.
                    next_node = current_node.next
                    current_node.next = None
                    next_node.prev = None
                    current_node = None
                    self.head = next_node
                    return
            elif current_node.data == key:
                # Case 3: If the node to be deleted is in between the list.
                if current_node.next:
                    # Case 3.1: If the node to be deleted is not the last node.
                    next_node = current_node.next
                    prev_node = current_node.prev
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    current_node.next = None
                    current_node.prev = None
                    current_node = None
                    return
                else:
                    # Case 3.2: If the node to be deleted is the last node.
                    prev_node = current_node.prev
                    prev_node.next = None
                    current_node.prev = None
                    current_node = None
                    return
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


d = DoublyLinkedList()
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.prepend(0)
d.delete_node(1)
d.delete_node(4)
d.print_list()
