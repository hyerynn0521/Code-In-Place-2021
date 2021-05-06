"""
TODO: Write a description here
"""

import random 

def main():
    #receives input from user of which number to start with
    hailstone = int(input("Enter a number: "))
    steps  = 0;
    #goal: get number to become 1
    while hailstone != 1:
        #if even, divide by half
        if hailstone%2 == 0:
            print(str(int(hailstone)) + " is even, so I take half: " + str(int(hailstone/2)))
            hailstone /= 2
        #if odd, 3n+1
        else:
            print(str(int(hailstone)) + " is odd, so I make 3n + 1: " + str(int(hailstone*3+1)))
            hailstone = 3*hailstone + 1
        #count steps
        steps += 1
    print("The process took " + str(steps) + " steps to reach 1")


if __name__ == "__main__":
    main()
