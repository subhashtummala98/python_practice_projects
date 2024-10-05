import random
# function for die roll
def Roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val,max_val)

    return roll

# no of players
while True:
    players = input("enter no of players between (2-4):")
    if players.isdigit():
        players=int(players)
        if 2<= players<=4:
            break
        else: print("enter between(2-4)")
    else:
        print("valid input")


max_score = 50  # maximum score for a player to win
player_score = [0 for _ in range(players)] # players initial scores

while max(player_score) < max_score:# checking players score
    for player_index in range(players):
        print("\nplayer number", player_index+1, "turn has started\n")
        current_score = 0
        while True:
            should_role = input("like to roll the dice again (y)")
            if should_role.lower() != "y":
                break
            value = Roll()

            if value == 1:
                print("you rolled 1 so your turn is done")
                current_score=0
                break
            else:
                current_score += value
                print("you rolled ", value)
            print("your score is", current_score)
        player_score[player_index] += current_score
        print("your total score", player_score[player_index])

max_score = max(player_score)
winning_score = player_score.index(max_score)
print("player no", winning_score+1 , "is the winner with score", max_score)
#print(player_score)