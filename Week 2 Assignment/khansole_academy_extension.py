"""
TODO: Write a description here
"""

import random

def main():
    correct = 0;
    #has to get three in a row correct
    while correct < 3:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        print("What is " +str(num1)+ " + "+ str(num2)+ "?")
        answer = int(input("Your answer: "))
        if answer == num1+num2:
            correct += 1
            print("Correct! You've gotten "+ str(correct) + " in a row.")
        else:
          #resets number of correct in a row if wrong answer
            correct = 0;
            print("Incorrect. The expected answer is " + str(num1+num2))
    print("Congratulations! You mastered addition.")
if __name__ == '__main__':
    main()
