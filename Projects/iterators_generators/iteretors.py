"""Practice iterators"""

"""1st create  iterator using iter and then use it to iterate over the list and using next() function"""

# list1 = [1, 2, 3, 4, 5]
# iterator = iter(list1)
#
# print(next(iterator))
# print(next(iterator))
#
# for i in iterator:
#     print(i)


"""2nd create a class with __iter__ and __next__ methods"""


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        else:
            self.index += 1
            return self.data[self.index - 1]


my_list = [1, 2, 3, 4, 5, 6]
my_iterator = MyIterator(my_list)

for i in my_iterator:
    print(i)
