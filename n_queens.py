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
def compatible(c1,queens):
    comp = True
    for k in queens:
        if attack(c1,k):
            comp = False
    return comp
def placequeens(size,queens):
    if len(queens) == size:
        return queens
    
    for i in range(size):
        if compatible([i,len(queens)],queens):
            queens.append([i,len(queens)])
            result = placequeens(size,queens)
            if result is not None:
                return result
            queens.pop()
