import random
def game():
    A_heads = 6
    B_heads = 4
    
    while A_heads<10 and B_heads<10:
        A_heads += random.randint(0,1)
        B_heads += random.randint(0,1)
        
    #end of the game
    
    if A_heads <= B_heads:
        return 0
    else:
        return 1

games = 1000
A_wins = 0

for i in range(games):
    A_wins += game()
    
print(A_wins)
print(A_wins/games)