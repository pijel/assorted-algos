class DoubleListNode:
    def __init__(self,x):
        self.val = x
        self.prev = None
        self.next = None
class kQueue:
    def __init__(self,size):
        self.first = None
        self.last = None
        self.limit = size
        self.size = 0
    def add(self,value):
        new_node = DoubleListNode(value)
        if self.first == None and self.last == None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.last
            self.last.prev = new_node
            self.last = new_node
        if self.size >= self.limit:
            self.remove()
        self.size +=1
     
    def remove(self):
        if not self.first:
            return False
        return_value = self.first.val
        self.first = self.first.prev
        self.size -=1
        return return_value
        
    def peek(self):
        return self.first.val
    def __str__(self):
        a = self.first
        num_eles = 0
        while a:
            print (a.val)
            a = a.prev
            num_eles +=1
        return 'End of Queue, {} elements found'.format(num_eles)
    def nonempty(self):
        return (self.first != None and self.last != None)