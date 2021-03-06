def newsourcesink(sources,sinks, graph):
    q = [i for i in sources]
    seen = set([])
    prev = [-1] * len(graph)
    while  q:
        current = q.pop(0)
        if current in sinks:
            i = current
            new_path = [current]
            while i not in sources:
                new_path.append(prev[i])
                i = prev[i]
            return new_path[::-1]           
        if current not in seen:
            seen.add(current)
            for i in range(len(graph[current])):
                if graph[current][i] > 0 and i not in seen :
                    q.append(i)
                    if prev[i] == -1:
                        prev[i] = current    
                    
    return -1
# the sources and sinks are guaranteed to be disjoint. if a shortest path is returned, it should be at least length 2
def edkarp(entrances,exits,path):
    shortest_path = newsourcesink(entrances,exits,path)
    m_flow = 0
    while shortest_path != -1:
        capacity = path[shortest_path[0]][shortest_path[1]]
        for i in range(len(shortest_path)-1):
            if path[shortest_path[i]][shortest_path[i+1]] < capacity:
                 capacity = path[shortest_path[i]][shortest_path[i+1]]
        m_flow += capacity
        for i in range(len(shortest_path)-1):
            path[shortest_path[i]][shortest_path[i+1]] -= capacity
            path[shortest_path[i+1]][shortest_path[i]] += capacity
        
        shortest_path = newsourcesink(entrances,exits,path)
    return m_flow
