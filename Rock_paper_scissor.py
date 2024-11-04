import random

emojies = {"r":"💎", "p": "📃", "s":"✂"}
choice = ("r", "p", "s")

while True:
    user_choice= input("Rock, Paper, Scisser?(r,p,s):  ")
    if user_choice not in choice:
        print("invalid choice")
        continue
        
    computer_choice = random.choice(choice)

    print(f'you choose {emojies[user_choice]}')
    print(f'computer choose {emojies[computer_choice]}')

    if user_choice == computer_choice:
        print("Tie")
    elif ((user_choice == 'r' and computer_choice == 's') or (user_choice == 's' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 'r')):
        print("you win")
    else:
        print("You Lose")

    should_continue = input("will you continue?(y/n):  ").lower()

    if should_continue != 'y':
        break