import pytest
from controllers.game_move import GameMove

@pytest.fixture()
def test_maze():
    return GameMove('Maze','Maze',0)

def test_maze_controller(test_maze):
    """
    Test the class to have the correct attribute value set up
    """
    assert test_maze.maze == 'Maze'
    assert test_maze._name == 'Maze'
    assert test_maze.timer == 0