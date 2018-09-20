class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        return get_cycles(M)
        
def get_connected_component(M,ind):
    seen_nodes = set([])
    seen_nodes.add(ind)
    
    queue = [ind]
    while len(queue) > 0:
        index = queue.pop(0)
        for i in range(len(M[index])):
            if M[index][i] == 1 and i not in seen_nodes:
                seen_nodes.add(i)
                queue.append(i)
    return seen_nodes
            
    
def get_cycles(M):
    unseen_nodes = set([])
    for i in range(len(M[0])):
        unseen_nodes.add(i)
        
    cycles_found = 0
    
    while len(unseen_nodes)>0:
        next_ele = unseen_nodes.pop()
        cycle = get_connected_component(M,next_ele)
        cycles_found += 1
        
        unseen_nodes -= cycle
        
    return cycles_found
        