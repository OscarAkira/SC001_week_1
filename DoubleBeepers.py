"""
File: DoubleBeepers.py
Name:Oscar
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers at street 1, avenue 2
    """
    move()
    double()
    go_home()


def double():
    """
    Pre-condition: Karel is at (1, 2) facing East
    Post-condition: The number of beepers at (1, 2) is doubled
    """
    pick_one_put_two()
    move_back()


def pick_one_put_two():
    """
    Pre-condition: Karel is at (1, 2) facing East with known number of beepers
    Post-condition: Karel is at (1, 2) facing East with double beepers at (1, 3)
    """
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()
        move()
        turn_around()


def turn_around():
    """
    Karel turns left 2 times
    """
    turn_left()
    turn_left()


def move_back():
    """
    Pre-condition: Karel is at (1, 2) facing East
                   Beepers are at (1, 3)
    Post-condition: Karel is at (1, 3) facing East
                    Beepers are at (1, 2)
    """
    move()
    while on_beeper():
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        turn_around()
        move()


def go_home():
    """
    Pre-condition: Karel is at (1, 3) facing East
    Post-condition: Karel is at (1, 1) facing East
    """
    while not facing_west():
        turn_left()
    while front_is_clear():
        move()
    turn_around()

####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)