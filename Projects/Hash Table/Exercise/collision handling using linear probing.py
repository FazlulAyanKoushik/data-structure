"""Collision handling using linear probing in hash table"""


class HashTable:
    def __init__(self):
        self.size = 10
        self.MAX = 10
        self.arr = [None for i in range(self.size)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def get_probe_index(self, index, i):
        return (index + i) % self.MAX

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        if self.arr[index] is None:
            self.arr[index] = (key, value)
        else:
            i = 1
            while True:
                new_index = self.get_probe_index(index, i)
                if index == new_index:
                    print(f"Hash table is full for key: {key}")
                    break
                if self.arr[new_index] is None:
                    self.arr[new_index] = (key, value)
                    break
                i += 1

    def __getitem__(self, key):
        index = self.get_hash(key)
        if self.arr[index] is None:
            return
        if self.arr[index][0] == key:
            return self.arr[index][1]
        else:
            i = 1
            while True:
                new_index = self.get_probe_index(index, i)
                if index == new_index:
                    return
                if self.arr[new_index] is None:
                    return
                if self.arr[new_index][0] == key:
                    return self.arr[new_index][1]
                i += 1


t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 670
t["march 17"] = 67
t["march 18"] = 671
t["march 27"] = 672
t["march 28"] = 673
t["march 37"] = 674
t["march 38"] = 675
t["march 47"] = 676
t["march 48"] = 677

print(t.arr)

print(t["march 18"])
