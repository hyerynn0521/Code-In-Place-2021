from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    pass
    while front_is_clear():
        put_beeper()
        climb_half_slope()
    put_beeper()

def climb_half_slope():
    turn_left()
    move()
    turn_right()
    move()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
if __name__ == '__main__':
    run_karel_program('RampKarel1.w')
