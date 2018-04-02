class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if dungeon == None:
            return 1
        if len(dungeon) == 1:
            min_hp = [dungeon[0][0]]
            for i in range(1,len(dungeon[0])):
                min_hp.append(min_hp[-1]+dungeon[0][i])
            if -min(min_hp)>0:
                return -min(min_hp) +1
            return 1
        return minHealth(dungeon)

        
def subsets(n,k):
    if k == 0:
        return [[]]
    if k == 1:
        return [[i] for i in range(n)]
    if k > n/2:
        full = [ i for i in range (n)]
        new_ele = []
        for i in subsets(n,n-k):
            diff = [j for j in full if j not in i]
            new_ele.append(diff)
        return new_ele
    else:
        new_ele = []
        for i in subsets(n,k-1):
            for j in range(n):
                if j > max(i):
                    new_ele.append(i+[j])
        return new_ele
        
def minHealth(dungeon):
    n = len(dungeon[0])-1
    m = len(dungeon)-1
    right_moves = subsets(n+m,n)
    min_hp = 1000
    
    for i in right_moves:
        position = [0,0]
        hp = [dungeon[0][0]]
        k = 0 
        while k < n+m:
            #print(position)                   
            if k in i:
                position[1] += 1
            else:
                position[0] += 1
            
            hp.append(hp[-1] + dungeon[position[0]][position[1]])
            
            k+=1
        #print(i,hp)
        path_hp = min(hp)
        if -path_hp < min_hp:
            min_hp = -path_hp
    if min_hp<=0:
        return 1
    return (min_hp) +1 


        