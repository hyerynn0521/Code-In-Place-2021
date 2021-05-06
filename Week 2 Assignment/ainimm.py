# game of nimm: 20 stones, players can remove 1 or 2 stones, last one to take the stone loses
# A Program where the computer wins the game of nimm every time

def main():
    stone = 20
    turn1 = False
    computer = True
    remove = 0
    inputisinvalid = False
    while stone > 0:
        print("There are " + str(stone) + " stones left")
        if turn1:
            computer = True
            turn1 = False
            remove = int(input("Player would you like to remove 1 or 2 stones? "))
        elif computer:
            turn1 = True
            computer = False
            
            if remove == 1:
                remove = 2
                print("Computer removed 2 stones")
            else:
                remove = 1
                print("Computer removed 1 stone")
        inputisinvalid = remove < 1 or remove > 2
        while inputisinvalid:
            remove = int(input("Please enter 1 or 2: "))
            inputisinvalid = remove < 1 or remove > 2
        stone -= remove
        print("")
    if turn1:
        print("Player wins!")
    else:
        print("Computer wins!") 












if __name__ == "__main__":
    main()
