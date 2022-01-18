# Challenge yourself and practice learning from outside resources
# by following this tutorial to build a maze generator:
# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e

# unvisited blocks will be 'u'

# Maze generator -- Randomized Prim Algorithm

## Imports
import random
import time
from colorama import init
from colorama import Fore, Back, Style

# random spot and then another random spot and then check the walls adjacent to it
## Functions
def printMaze(maze):
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == 'u'): # what does this do?
                print(Fore.WHITE + str(maze[i][j]), end=" ") #if unvisited then white
            elif (maze[i][j] == 'c'):
                print(Fore.GREEN + str(maze[i][j]), end=" ") #if cell then green
            else:
                print(Fore.RED + str(maze[i][j]), end=" ") # if wall then red and what doe str(maze[i][i]) print?

        print('\n')

# Make the wall a passage and mark the unvisited cell as part of the maze
# Find number of surrounding cells
# number that gives. Looking in maze and checking each cell around the random wall then if
# checking each of the 4 adjancent cell then return to number of ajecent cells
def surroundingCells(rand_wall):
    s_cells = 0
    if (maze[rand_wall[0] - 1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0] + 1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1] - 1] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1] + 1] == 'c'):
        s_cells += 1

    return s_cells


## Main code
# Init variables
wall = 'w'
cell = 'c'
unvisited = 'u'
height = 11
width = 27
maze = []

# Initialize colorama
init() # why does this need to be initialized?

# Denote all cells as unvisited
for i in range(0, height):
    line = []
    for j in range(0, width):
        line.append(unvisited)
    maze.append(line)

# Randomize starting point and set it a cell
starting_height = int(random.random() * height)
starting_width = int(random.random() * width)
if (starting_height == 0):
    starting_height += 1
if (starting_height == height - 1):
    starting_height -= 1
if (starting_width == 0):
    starting_width += 1
if (starting_width == width - 1):
    starting_width -= 1

# Mark it as cell and add surrounding walls to the list
#appended
#makes it a wall
maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height - 1, starting_width])
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])



# from this array of array. Getting array at position -1 and then starting width
# height array of 4 and then each of the element and the another array of size 4
# Denote walls in maze
#setting the position to w
#just printing it out to terminal
maze[starting_height - 1][starting_width] = 'w'
maze[starting_height][starting_width - 1] = 'w'
maze[starting_height][starting_width + 1] = 'w'
maze[starting_height + 1][starting_width] = 'w'


# while elements exist
#picking a random position in walls array of the 4 cells then picking random one
while (walls):
    # Pick a random wall
    rand_wall = walls[int(random.random() * len(walls)) - 1]
#wall is an array of of array
    # Check if it is a left wall
    if (rand_wall[1] != 0): # if y position doesn't equal zero
        if (maze[rand_wall[0]][rand_wall[1] - 1] == 'u' and maze[rand_wall[0]][rand_wall[1] + 1] == 'c'): # then it isn't on the left most border
            # Find the number of surrounding cells
            s_cells = surroundingCells(rand_wall)

            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                # Mark the new walls
                # Upper cell
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0] - 1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0] - 1][rand_wall[1]] = 'w'
                    if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0] - 1, rand_wall[1]])

                # Bottom cell
                if (rand_wall[0] != height - 1):
                    if (maze[rand_wall[0] + 1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0] + 1][rand_wall[1]] = 'w'
                    if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0] + 1, rand_wall[1]])

                # Leftmost cell
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1] - 1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1] - 1] = 'w'
                    if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1] - 1])

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

            continue

    # Check if it is an upper wall
    if (rand_wall[0] != 0):
        if (maze[rand_wall[0] - 1][rand_wall[1]] == 'u' and maze[rand_wall[0] + 1][rand_wall[1]] == 'c'):

            s_cells = surroundingCells(rand_wall)
            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                # Mark the new walls
                # Upper cell
                #unensuring not top most cell # left?
                # if doesn't equal c then making it a wall
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0] - 1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0] - 1][rand_wall[1]] = 'w'
                        # if that wall is not in list of walls then add to list of walls
                    if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0] - 1, rand_wall[1]])

                # Leftmost cell
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1] - 1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1] - 1] = 'w'
                    if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1] - 1])

                # Rightmost cell
                if (rand_wall[1] != width - 1):
                    if (maze[rand_wall[0]][rand_wall[1] + 1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1] + 1] = 'w'
                    if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1] + 1])

            # Delete wall
            #looping through each wall and current cell is in wall then remove it
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

            continue

    # Check the bottom wall
    if (rand_wall[0] != height - 1):
        if (maze[rand_wall[0] + 1][rand_wall[1]] == 'u' and maze[rand_wall[0] - 1][rand_wall[1]] == 'c'):

            s_cells = surroundingCells(rand_wall)
            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                # Mark the new walls
                if (rand_wall[0] != height - 1):
                    if (maze[rand_wall[0] + 1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0] + 1][rand_wall[1]] = 'w'
                    if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0] + 1, rand_wall[1]])
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1] - 1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1] - 1] = 'w'
                    if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1] - 1])
                if (rand_wall[1] != width - 1):
                    if (maze[rand_wall[0]][rand_wall[1] + 1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1] + 1] = 'w'
                    if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1] + 1])

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

            continue

    # Check the right wall
    if (rand_wall[1] != width - 1):
        if (maze[rand_wall[0]][rand_wall[1] + 1] == 'u' and maze[rand_wall[0]][rand_wall[1] - 1] == 'c'):

            s_cells = surroundingCells(rand_wall)
            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                # Mark the new walls
                if (rand_wall[1] != width - 1):
                    if (maze[rand_wall[0]][rand_wall[1] + 1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1] + 1] = 'w'
                    if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1] + 1])
                if (rand_wall[0] != height - 1):
                    if (maze[rand_wall[0] + 1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0] + 1][rand_wall[1]] = 'w'
                    if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0] + 1, rand_wall[1]])
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0] - 1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0] - 1][rand_wall[1]] = 'w'
                    if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0] - 1, rand_wall[1]])

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

            continue

    # Delete the wall from the list anyway
    for wall in walls:
        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
            walls.remove(wall)

# Mark the remaining unvisited cells as walls
#loop over entire maze and everything u is a wall
for i in range(0, height):
    for j in range(0, width):
        if (maze[i][j] == 'u'):
            maze[i][j] = 'w'

# Set entrance and exit
for i in range(0, width):
    if (maze[1][i] == 'c'):
        maze[0][i] = 'c'
        break

for i in range(width - 1, 0, -1):
    if (maze[height - 2][i] == 'c'):
        maze[height - 1][i] = 'c'
        break

# Print final maze
printMaze(maze)

# x position and y position
# magic numbers
