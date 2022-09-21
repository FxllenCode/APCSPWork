import random
import math

player1 = input("What is the name of player 1? ")
player2 = input("What is the name of player 2? ")

number = 10
counter1 = 0
counter2 = 0

while True:
    counter1 += 1
    counter2 += 1
    guess1 = int(input(player1 + ", what is your guess? (1-100)"))
    guess2 = int(input(player2 + ", what is your guess? (1-100)"))
    if guess1 == number:
        print(
            player1
            + ", you won! Congrats! It took you "
            + str(counter1)
            + " tries to win!"
        )
        break

    elif guess2 == number:
        print(
            player2
            + ", you won! Congrats! It took you "
            + str(counter1)
            + " tries to win!"
        )
        break
    print("Wrong! Try again!")
