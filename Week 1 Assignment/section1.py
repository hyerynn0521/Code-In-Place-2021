from karel.stanfordkarel import *

# File: HospitalKarel.py
# -----------------------------
# Here is a place to program your Section problem
# A program for Karel to build a hospital

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        find_beeper()
        build_hospital()
    turn_around()
    while front_is_clear():
        move()
    turn_around()

if __name__ == '__main__':
    run_karel_program('HospitalKarel.w')
def turn_around():
    for i in range (2):
        turn_left()
def build_hospital():
    turn_left()
    for i in range (2):
        move()
        put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    for i in range (2):
        move()
        put_beeper()
    turn_left()
    if front_is_clear():
        move()



def find_beeper():
    while no_beepers_present():
        move()

def turn_right():
    for i in range (3):
        turn_left()
