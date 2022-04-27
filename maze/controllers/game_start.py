from models.maze import Maze
from models.player import Player
from .game_move import GameMove
from views.maze_view import MazeView
import datetime

class GameStart:
    """
    Creates an instance of the the game to be run
    """

    def __init__(self, maze, name=""):
        """
        instantiates the game and applies a Maze instance as an attribute.

        :param maze: An instance of the Maze class
        :type maze: class
        :param name: Name of a player
        :type maze: string
        """
        self.maze = Maze(maze)
        self._name = name

    def run(self):
        """
        Starts the actual game by creating a view of the maze attribute tied to a variable
        and then running the display_maze method to show the view.
        """
        start = MazeView(self.maze, self._name)

        start.display_maze()