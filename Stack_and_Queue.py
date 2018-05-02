 class ListNode:
    def __init__(self, x): 
        self.val = x
        self.next = None
class Stack:
    def __init__(self):
        self.head = head
    def push(self,value):
        new_node = ListNode(value)
        if self.head == None:
            self.head = new_node
            self.head.next = None
        else:
            new_node.next = self.head
            self.head = new_node
    def pop(self):
        if not self.head:
            return False
        return_value = self.head.val
        self.head = self.head.next
        return return_value
    def show(self):
        a = self.head
        while a:
            print(a.val)
            a = a.next
            
        
class DoubleListNode:
   def __init__(self,x):
       self.val = x
       self.prev = None
       self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    def add(self,value):
        new_node = DoubleListNode(value)
        if self.first == None and self.last == None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.last
            self.last.prev = new_node
            # if we wanted to used single linked lists, this would just be a second linked list pointing in the opposite direction. I think this is better
            self.last = new_node
    def remove(self):
        if not self.first:
            return False
        return_value = self.first.val
        self.first = self.first.prev
        return return_value
    def show(self):
        a = self.first
        while a:
            print (a.val)
            a = a.prev
