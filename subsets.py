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