"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

class Queue(object): 
    def __init__(self, limit = 10):
        self.queue = []
        self.front = None
        self.rear = None
        self.limit = limit
        self.size = 0
        # self.storage = ?
    
    def __len__(self):
        return self.size

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    def isEmpty(self):  
        return self.size <= 0
    
    def enqueue(self, value): # to add rear end of the queue (poner cola)
        if self.size >= self.limit:
            return -1          #overflow
        else:
            self.queue.append(value)
                
        if self.front is None:  #the rear as size of the queue and front as 0
            self.front = self.rear = 0
        else:
            self.rear = self.size
            
        self.size += 1
        
    def dequeue(self): # to pop, front end of the queue (remoder cola)
        if self.isEmpty():
            return -1          #underflow
        else:
            self.queue.pop()
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = 0
            else:
                self.rear = self.size - 1
    
    def getSize(self):
        return self.size