import random as M
guess = M.randint(1,100)

while True:
    number = int(input("enter no between 1 to 100:  "))
    if 1<=number<=100:
        print("good great number ")
        #break
    else:
        print("invalid number, enter no between 1 to 100") 

#while True:
    if number>guess:
        print("high than the guess number")
    elif number<guess:
        print("Lower than the guess number")
    elif number == guess:
        print("Congragulation, you gessed the number")
        break

