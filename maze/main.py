from models.maze import Maze 
from controllers.game_start import GameStart

if __name__ == "__main__":
  """
  The method to run the program
  """
  name = input("Enter player name: ")
  game = GameStart("maze.txt", name)
  game.run()