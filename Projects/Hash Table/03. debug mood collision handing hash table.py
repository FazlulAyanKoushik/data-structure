class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        index = self.get_hash(key)
        return self.arr[index]

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[index]):
            print("element :", element)
            print("element length:", len(element))
            if len(element) == 2 and element[0] == key:
                self.arr[index][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[index].append((key, value))


t = HashTable()

t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 67
