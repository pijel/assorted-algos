import random
def game2():
    A_points = 6
    B_points = 4
    
    while A_points < 10 and B_points< 10:
        flip = random.randint(0,1)
        if flip == 1:
            B_points += 1
        else:
            A_points += 1
    
    if A_points == 10:
        return 1
    return 0

games = 10000
A_wins = 0

for i in range(games):
    A_wins += game2()
    
print(A_wins)
print(A_wins/games)