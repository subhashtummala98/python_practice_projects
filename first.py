import random as M

def dice_roll():
    roll = M.randint(1,6)

    return roll


rolls = []

while True:
    play = input("do you want to play (y/n)?")
    if play == "y":
        for i in range(2):
            roll = dice_roll()
            rolls.append(roll)
        print(rolls)
    elif play == "n":
        print("Thanks for playing")
        break

