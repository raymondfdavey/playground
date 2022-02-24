import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import random

maze1 = np.array([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0],[0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],[0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],[0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],[0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0],[0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

class ShannonsMaze:
    def __init__(self, maze, startPosition, endPosition):
        self.originalMaze = np.copy(maze)
        self.workingMaze = np.copy(maze)
        self.showBlankMaze()
        self.startPosition = startPosition
        self.endPosition = endPosition
        self.currentPosition = startPosition
        self.showCurrentMazeState()
        self.height = maze.shape[0]
        self.width = maze.shape[1]
        self.nextSquare = (0,0)
        self.isMazeSolved = False
        self.solvedAgain = False

    def showBlankMaze(self):
        fig = plt.figure(figsize=(8,8))
        plt.imshow(self.originalMaze)
        plt.show()
    
    def showWorkingMazestate(self):
        fig = plt.figure(figsize=(8,8))
        plt.imshow(self.workingMaze)
        plt.show()

    def showCurrentMazeState(self):
        mazeForDisplay = np.copy(self.originalMaze)
        mazeForDisplay[self.currentPosition] = 8
        mazeForDisplay[self.endPosition] = 10
        fig = plt.figure(figsize=(8,8))
        plt.imshow(mazeForDisplay)
        plt.show()
    
    def checkUp(self):
        row = self.currentPosition[0] - 1
        col = self.currentPosition[1]
        print(row)
        print(col)
        if row < 0 or row > self.height: 
            return (0, 0)
        if col < 0 or col > self.width:
            return (0, 0)
        else:
            return (self.workingMaze[row, col], (row, col))
    
    def checkRight(self):
        row = self.currentPosition[0]
        col = self.currentPosition[1] + 1
        if row < 0 or row > self.height: 
            return (0, 0)
        if col < 0 or col > self.width:
            return (0, 0)
        else:
            return (self.workingMaze[row, col], (row, col))
    def checkLeft(self):
        row = self.currentPosition[0]
        col = self.currentPosition[1] - 1
        if row < 0 or row > self.height: 
            return (0, 0)
        if col < 0 or col > self.width:
            return (0, 0)
        else:
            return (self.workingMaze[row, col], (row, col))

    def checkDown(self):
        row = self.currentPosition[0] + 1
        col = self.currentPosition[1]
        if row < 0 or row > self.height: 
            return (0, 0)
        if col < 0 or col > self.width:
            return (0, 0)
        else:
            return (self.workingMaze[row, col], (row, col))
    
    def searchOptions(self):
        return {"UP": self.checkUp(), "DOWN": self.checkDown(),"LEFT": self.checkLeft(), "RIGHT": self.checkRight()}
    
    def solveMaze(self):
        while self.isMazeSolved == False:
            self.move()
    
    def move(self):
        results = self.searchOptions()
        resultsValues = [value[0] for value in list(results.values()) if value[0] != 0]
        print("VALUES:", resultsValues)
        options = [value for value in list(results.values()) if value[0] == 1]
        if len([value[1] for value in list(results.values()) if value[1] == self.endPosition]) == 1:
            self.workingMaze[self.currentPosition] = 2
            self.currentPosition = self.endPosition
            self.isMazeSolved = True
            self.solvedAgain = True
            self.showWorkingMazestate()
        elif len(options) == 1:
            self.nextSquare = options[0][1]
            self.workingMaze[self.currentPosition] = 2
            self.currentPosition = self.nextSquare
        elif len(options) > 1:
            choice = random.randint(0, len(options)-1)
            print(choice)
            self.nextSquare = options[choice][1]
            self.workingMaze[self.currentPosition] = 2
            self.currentPosition = self.nextSquare
        elif len(options) == 0:
            newOptions = [value for value in list(results.values()) if value[0] == 2]
            self.nextSquare = newOptions[0][1]
            self.workingMaze[self.currentPosition] = 5
            self.currentPosition = self.nextSquare
        self.showCurrentMazeState()

    def solveCompletedMaze(self, newStartPoint):
        self.isMazeSolved = False
        self.solvedAgain = False
        self.currentPosition = newStartPoint
        self.showCurrentMazeState()
        self.showWorkingMazestate()


        while self.solvedAgain == False:
            self.move()

    def solveAgainMove(self):
        print("MOVING")
    








# need to make it so that if options are all 5's and 1 two, then mark the square 4 and

newMaze = ShannonsMaze(maze1, (0, 2), (7, 9))

newMaze.move()
newMaze.solveMaze()
newMaze.showWorkingMazestate()
newMaze.solveCompletedMaze((6, 1))
# once completed need to switch algorithm to just follow the 2s


# seach step - check 4 directions
# choose direction step
# move step - includes marking the previous step as travelled to and also if it was a decision point
# repeat





    
#     aboveBelowLeftRight = (0,1,0,0)
#     move left 
#     move right
#     move up 
#     move down
#     check surroundings
#     mark decision pointer
#     markas visited
#     complete = False





# needs to store decision point, then mark all visited squares.
# once it reaches a dead end it goes to last decision point and tries the direction not marked as visited
# 1 = clear, 2= current position, 3 =finish, 4 = visited, 0 = barrier
# to be able to solve instantly from anywhere --- need to represent correct path and direction somehow
# once dead end is reached all squares then passed over need to be closed off as wrong
# or just needs to record decision points? like the direction to go 

# maybe have 'move left move right move up move down commands which change the current position
# store decision points? store maze complete? not sure
# cool project 

# really there should be a class that takes a maze and the start position as its arguments, it then should have a solve method which, after completion turns the status of the instance to 'solved'
# during solving it should print where it is after each move
# It should then have a "resolve" method with a new start position that see the players just go direct to solve 
# Fore each step should create an "above, below, left right" value tuple and if more than one is 1....