"""
TODO: Write a description here
"""

import random

def main():
    #start with 20 stone
    stone = 20
    #variables to determine which player's turn
    turn1 = True
    turn2 = False
    remove = 0
    inputisinvalid = False
    #while there are stones
    while stone > 0:
        
        print("There are " + str(stone) + " stones left")
        if turn1:
          #after player 1's turn, change booleans to indicate it's player 2's turn next
            turn2 = True
            turn1 = False
            remove = int(input("Player 1 would you like to remove 1 or 2 stones? "))
        elif turn2:
          #after player 2's turn, change booleans to indicate it's player 1's turn next
            turn1 = True
            turn2 = False
            remove = int(input("Player 2 would you like to remove 1 or 2 stones? "))
        #check if input is invalid
        inputisinvalid = remove < 1 or remove > 2
        while inputisinvalid:
            #prompt for input until user inputs valid input
            remove = int(input("Please enter 1 or 2: "))
            inputisinvalid = remove < 1 or remove > 2
        #remove stone
        stone -= remove
        print("")
    #after game ends, determine the winner
    if turn1:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
if __name__ == '__main__':
    main()
