
from karel.stanfordkarel import *

"""
File: CleanupKarel.py
--------------------
When you finish writing this file, CleanupKarel should be able to
pick up all beepers from the first row of any sized world and
end in the bottom right corner facing East.
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
        check_and_pick()
        move()
    check_and_pick()
    
def check_and_pick():
    if beepers_present():
        pick_beeper()


    

if __name__ == '__main__':
    run_karel_program('Cleanup1.w')
