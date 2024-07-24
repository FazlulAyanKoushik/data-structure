class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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
            return True

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            print("Empty Linked list")
            return False
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return True

        temp = self.head
        previous_node = None
        while temp.next:
            previous_node = temp
            temp = temp.next

        previous_node.next = None
        self.tail = previous_node
        self.length -= 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node
            self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            print("Empty Linked list")
            return False
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            new_head = self.head.next
            self.head = new_head
            self.length -= 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            print("index out of range")
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp, temp.value

    def set_value(self, index, value):
        temp, _ = self.get(index)
        if temp:
            temp.value = value
            return True

        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("index out of range")
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp, _ = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            print("index out of range")
            return False

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        previous_node, _ = self.get(index - 1)
        del_node = previous_node.next
        previous_node.next = del_node.next
        del_node.next = None
        self.length -= 1
        return True

    def print_list(self):
        if self.length == 0:
            print("Empty Linked list")
            return False

        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print("")

    def reverse(self):
        if self.length == 0:
            print("Empty Linked list")
            return False

        before = None
        temp = self.head
        self.head = self.tail
        self.tail = temp
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True


if __name__ == "__main__":
    my_linked_list = LinkedList()
    my_linked_list.append(4)
    my_linked_list.append(6)
    my_linked_list.append(7)
    my_linked_list.append(8)
    my_linked_list.append(5)
    my_linked_list.print_list()
    my_linked_list.insert(5, 10)
    my_linked_list.print_list()
