import pytest
from controllers.game_start import GameStart
@pytest.fixture()
def test_maze():
    return GameStart('maze.txt','Maze')

def test_maze_controller(test_maze):
    """
    Test the class to have the correct attribute set up
    """
    assert hasattr(test_maze, 'maze')
    assert hasattr(test_maze, '_name')
    assert hasattr(test_maze, 'run')





