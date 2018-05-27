import math
def dijikstra(graph,start,end):
    #unseen_nodes is really unfinished_nodes
    finished_nodes = {}
    finished_nodes[start] = 0
    unseen_nodes = {}
    for i in range(len(graph)):
        unseen_nodes[i] = math.inf
    unseen_nodes[start] = 0
    while end not in finished_nodes:
        min_Node = -1
        for i in unseen_nodes:
            if min_Node == -1:
                min_Node = i
            elif unseen_nodes[min_Node] > unseen_nodes[i]:
                min_Node = i
        
        finished_nodes[min_Node] = unseen_nodes[min_Node]
        saved_distance = unseen_nodes[min_Node]
        unseen_nodes.pop(min_Node)
        for i in range(len(graph[min_Node])):
            if graph[min_Node][i] > 0:
                if i in unseen_nodes:
                    if saved_distance + graph[min_Node][i] < unseen_nodes[i]:
                        unseen_nodes[i] = saved_distance + graph[min_Node][i]
                       
    return finished_nodes[end]