class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return new_node

        prev_node = self.tail
        prev_node.next = new_node
        self.tail = new_node
        self.tail.prev = prev_node
        self.length += 1
        return new_node

    def pop(self):
        if self.length == 0:
            print("Empty doubly linked list")
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1

        temp: Node | None = self.tail
        prev_node = temp.prev
        self.tail = prev_node
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return new_node

        temp = self.head
        self.head = new_node
        self.head.next = temp
        temp.prev = self.head
        self.length += 1
        return new_node

    def pop_first(self):
        if self.length == 0:
            print("Empty doubly linked list")
            return None

        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        temp = self.head
        self.head = temp.next
        self.head.prev = None
        temp.next = None
        self.length -= 1
        return temp

    def get_node(self, index):
        if index < 0 or index >= self.length:
            print("index out of range")
            return None

        temp: Node | None = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_node(self, index, value):
        node = self.get_node(index)
        if node is not None:
            node.value = value
            return node
        else:
            return None

    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("index out of range")
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        else:
            after_node = self.get_node(index)
            new_node = Node(value)
            prev_node = after_node.prev
            prev_node.next = new_node
            new_node.prev = after_node.prev
            new_node.next = after_node
            after_node.prev = new_node
            self.length += 1
            return new_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            print("index out of range")
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next

            prev_node = temp.prev
            after_node = temp.next
            prev_node.next = after_node
            after_node.prev = prev_node
            temp.next = None
            temp.prev = None
            self.length -= 1
            return temp

    def print_list(self):
        if self.length == 0:
            print("Empty doubly linked list")
            return False

        temp = self.head
        for _ in range(self.length):
            print(temp.value, end=" ")
            temp = temp.next
        print("")
        return True


if __name__ == "__main__":
    my_dll = DoublyLinkedList()
    my_dll.append(4)
    my_dll.append(6)
    my_dll.append(12)
    my_dll.append(13)
    my_dll.print_list()
    my_dll.insert(3, 11)
    my_dll.print_list()
    my_dll.remove(3)
    my_dll.print_list()
