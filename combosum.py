class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        k = combosum(candidates,target)
        k.sort()
        return k
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

    
def combosum(candidates,target):
    candidates.sort()
    q = Queue()
    answer = []
    for i in candidates:
        q.add([i])
    
    while q.nonempty():
        current = q.remove()
        
        if sum(current) == target:
            answer.append(current)
        else:
            new_candidates = [current +[i] for i in candidates if i >= max(current)]
            for k in new_candidates:
                if sum(k) < target:
                    q.add(k)
                elif sum(k) == target:
                    answer.append(k)
                
        
    return answer