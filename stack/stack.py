"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []
        # self.storage = ?

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)
        self.size += 1
        print(self.storage)
        print(len(self.storage))

    def pop(self):
        if len(self.storage) > 0:
            popped_value = self.storage.pop()
            self.size -= 1
            print(self.storage)
            print(len(self.storage))
            return popped_value
        else:
            print('flag')
            return None

