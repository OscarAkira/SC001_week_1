"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:Oscar
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    Pre-condition: Karel is at the left side of the wall, facing East
    Post-condition: Karel is at the button , facing East
    """
    up()
    cross()
    down()


def down():
    """
    Pre-condition: Karel is at right side of the wall, facing South.
    Post-condition:
    """
    while front_is_clear():
        move()
    turn_left()


def cross():
    """
    Pre-condition: Karel is at the left side of the wall, facing East
    Post-condition: Karel is at right side of the wall, facing South.
    """
    move()
    turn_right()


def up():
    """
    Pre-condition: Karel is at the left side of the wall, facing East
    Post-condition: Karel is facing East
    """
    while not front_is_clear():
        turn_left()
        # Karel is facing North
        move()
        turn_right()


def turn_right():
    """
    Karel turn left 3 times
    """
    turn_left()
    turn_left()
    turn_left()











####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
