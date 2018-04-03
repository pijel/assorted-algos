import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.dic = {}
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.array.append(val)
        if val not in self.dic:
            self.dic[val] = set([len(self.array)-1])
            return True
        else:
            self.dic[val].add(len(self.array)-1)
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        
        index = self.dic[val].pop()
        self.array[index] = self.array[-1]
        self.dic[self.array[-1]].add(index)
        self.dic[self.array[-1]].remove(len(self.array)-1)
        self.array.pop()
        
        if len(self.dic[val]) == 0:
            del self.dic[val]
        
        
        return True
        
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.array[random.randint(0,len(self.array)-1)]
        