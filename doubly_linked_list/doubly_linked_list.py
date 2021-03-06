import os

print(os.path.realpath("doubly_linked_lists.py"))

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode: #create class
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value): #After + current
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value): #before + current
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self): #delete  End
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):  #new head + node
        new_node = ListNode(value, None, None)
        self.length += 1

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
            self.max = value

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self): #remove list -> to see next node + return value
        if self.head: 
            value = self.head.value
            print("supress from tail", value, "length", self.length)
            self.delete(self.head)
            return value
        else:
            return

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):  #new tail
        new_node = ListNode(value, None, None) #start
        self.length += 1
        print("incorporate to tail", value, "length", self.length)

        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
            self.max = value #End

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self): #start
        value = self.tail.value
        self.delete(self.tail)
        return value #End

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head: #start
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value) #End

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if not self.head:
            print("Empty list")
            return

        self.length -= 1

        if self.head == self.tail:
            self.head = None
            self.tail = None

        if node == self.head:
            self.head = node.next
            self.head.prev = None

        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None

        node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head == self.tail:
            return self.head.value

        max = 0
        curr_node = self.head

        while True:

            if curr_node.value > max:
                max = curr_node.value

            if curr_node.next == None:
                break
            else:
                curr_node = curr_node.next

        return max