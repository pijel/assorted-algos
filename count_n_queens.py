class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n== 0:
            return 1
        return countqueens(n)

def countqueens(board_dim):
    q = Queue()
    answer = []
    for i in range(board_dim):
        q.add([(i,0)])
    while q.nonempty():
        current = q.remove()
        if len(current) == board_dim:
            answer.append(current)
        else:
            for i in range(board_dim):
                if compatible ((i,len(current)),current):
                    k = current + [(i,len(current))]
                    q.add(k)
    return len(answer)

def compatible(c1,queens):
    comp = True
    for k in queens:
        if attack(c1,k):
            comp = False
    return comp

def attack(c1,c2):
    if c1[0] == c2[0]:
        return True
    #this checks the rows
    if c1[1] == c2[1]:
        return True
    #columns
    if c1[1] - c1[0] == c2[1] - c2[0]:
        return True
    #diagonal
    if c1[1] + c1[0] == c2[1] + c2[0]:
        return True
    #other diagonal
    return False

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
    def nonempty(self):
        return (self.first != None and self.last != None)

class DoubleListNode:
    def __init__(self,x):
        self.val = x
        self.prev = None
        self.next = None