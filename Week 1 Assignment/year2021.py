from karel.stanfordkarel import *

"""
File: 2021.py
--------------------
When you finish writing this file, Karel should be able to place 20 beepers,
then 21 beepers, and end facing East to the right of the 21 beepers.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    pass
    put_five_beepers()
    put_five_beepers()
    put_five_beepers()
    put_five_beepers()
    move()
    put_five_beepers()
    put_five_beepers()
    put_five_beepers()
    put_five_beepers()
    put_beeper()
    move()

def put_five_beepers():
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()

if __name__ == '__main__':
    run_karel_program()
