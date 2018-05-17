# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return total_tilt(root)
        
def totalsum(root):
    if not root:
        return 0
    if root and not root.left and not root.right:
        return root.val
    else:
        return root.val + totalsum(root.left) + totalsum(root.right)

def tilt(root):
    return abs(totalsum(root.left) - totalsum(root.right))

def total_tilt(root):
    q = Queue()
    if not root:
        return 0
    q.add(root)
    s = 0
    while q.nonempty():
        current = q.peek()
        s += tilt(current)
        
        if current.left:
            q.add(current.left)
        if current.right:
            q.add(current.right)
        q.remove()
    return s
        

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
    def nonempty(self):
        return (self.first != None and self.last != None)
    def peek(self):
        return self.first.val
    