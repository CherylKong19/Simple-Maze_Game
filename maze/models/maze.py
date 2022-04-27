
import csv, random
from .player import Player
from .score import Score

import pygame
import pygame.locals

class Maze:
    """Creates a maze from a text file
    """

    def __init__(self,filename):
        """Creates the instance of the maze

        :param filename: a text file composed of X's, spaces, and an E separated by commas
        :type filename: text file
        """
        with open(filename, 'r') as inputfile:
            content = list(csv.reader(inputfile))
        self.content = content
        """assigns the nested list derived from the file to an attribute of the instance
        """
        self.player = Player()
        """Creates an instance of player in the maze to move around and pick up items
        """
        self.location = self.player.location(self.content)
        """Tracks the location of the Player
        """
        self.complete = True

        i = 0
        while i < 4:
        # """Loops through spots randomly and places a key if the spot is empty
            found = True

            while found:
                line = random.choice(self.content)
                spot = random.randrange(0,len(line))

                if line[spot] == " ":
                    found = False
                    x = self.content.index(line)
                    y = spot
                    self.content[x][y] = "key"
                    i += 1

    def can_move_to(self, line, column):
        """Checks if it is possible to move to a part of the maze

        :param line: an index of the outer list
        :type line: index
        :param column: an index of the inner list
        :type column: index
        :return: returns whether the spot can be moved to
        :rtype: boolean
        """
        if self.content[line][column] != "X":
            if self.is_item(line, column) == True:
                return True
            else:
                return True
        else:
            return False

    def find_random_spot(self):
        """Finds a random spot to check if it can exist and is empty
        """
        found = True
        while found:
            line = random.choice(self.content)
            spot = random.randrange(0,len(line))

            if line[spot] != "X":
                found = False
                x = self.content.index(line)
                y = spot

        location = (x,y)
        return(location)

    def is_item(self, line, column):
        """Checks if a spot is an item

        :param line: index of the outer list
        :type line: index
        :param column: index of the inner list
        :type column: index
        :return: returns true if the spot is an item or "key"
        :rtype: boolean
        """
        if self.content[line][column] == "key":
            self.player.appendItem("key")

            self.content[line][column] = " "
            return True
        else:
            return False

    def is_exit(self, line, column):
        """Checks if a spot is the exit

        :param line: index of the outer list
        :type line: index
        :param column: index of the inner list
        :type column: index
        :return: returns true if the spot is the exit or "E"
        :rtype: boolean
        """
        if self.content[line][column] == "E":
            if len(self.player.backpack) == 4:
                print("\n\nCongratulations. You win!\n\n")
            else:
                self.complete = False
                print("\n\nYou lose. You didn't collect all the items!\n\n")

            return True
        else:
            return False