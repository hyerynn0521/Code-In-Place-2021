from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter code.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        fill_with_beepers()
        turn_around()
        go_to_bottom()
        turn_left()
        find_column()
        
        

    fill_with_beepers()
    turn_around()
    go_to_bottom()
    turn_left()
        

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
def go_to_bottom():

    while front_is_clear():
        move()

def fill_with_beepers():
    turn_left()
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
    if no_beepers_present():
        put_beeper()

def find_column():
    move()
    move()
    move()
    move()
if __name__ == '__main__':
    run_karel_program('SampleQuad1.w')
