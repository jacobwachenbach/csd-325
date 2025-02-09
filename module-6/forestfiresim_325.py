"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

import random
import time
import sys

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
LAKE = '~'
# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    lake_x_start, lake_x_end = WIDTH // 3, (WIDTH * 2) // 3
    lake_y_start, lake_y_end = HEIGHT // 3, (HEIGHT * 2) // 3
    
    # Create a lake in the center
    for x in range(lake_x_start, lake_x_end):
        for y in range(lake_y_start, lake_y_end):
            forest[(x, y)] = LAKE  # Fill with lake

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (x, y) not in forest and (random.random() * 100) <= INITIAL_TREE_DENSITY * 100:
                forest[(x, y)] = TREE  # Start as a tree.
            elif (x, y) not in forest:
                forest[(x, y)] = EMPTY  # Start as an empty space.
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                print('\033[92m' + TREE + '\033[0m', end='') # green
            elif forest[(x, y)] == FIRE:
                print('\033[91m' + FIRE + '\033[0m', end='') # red
            elif forest[(x, y)] == LAKE:
                print('\033[94m' + LAKE + '\033[0m', end='') # blue
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()


def main():
    forest = createNewForest()
    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'], 'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a previous iteration, just do nothing here:
                    continue

                if (forest[(x, y)] == EMPTY and random.random() <= GROW_CHANCE):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE
                elif (forest[(x, y)] == TREE and random.random() <= FIRE_CHANCE):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Ensure we don't spread fire into the lake
                            if (0 <= x + ix < forest['width'] and 0 <= y + iy < forest['height'] and 
                                forest.get((x + ix, y + iy)) == LAKE):
                                continue  # Skip if there's a lake
                            if (0 <= x + ix < forest['width'] and 0 <= y + iy < forest['height'] and 
                                forest.get((x + ix, y + iy)) == TREE):
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.