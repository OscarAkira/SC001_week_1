"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    Repeat 3 times from go-in, put beepers 99 times, and go-out.
    """
    for i in range (3):
        go_in()
        put_99()
        go_out()


def go_in():
    """
    pre-condition: Karel is at upper left on the pothole, facing east
    post-condition: Karel is in the pothole, facing south  
    """
    move()
    turn_right()
    move()


def turn_right():
    """
    Karel turn left 3 times
    """
    turn_left()
    turn_left()
    turn_left()


def put_99():
    """
    Karel put beeper 99 times.
    """
    for i in range(99):
        put_beeper()


def go_out():
    """
    pre-condition: Karel is in the pothole, facing south
    post-condition: Karel is at upper left on the pothole, facing east
    """
    turn_around()
    move()
    turn_right()
    move()


def turn_around():
    """
    Karel turn her face to opposite direction.
    """
    turn_left()
    turn_left()















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
