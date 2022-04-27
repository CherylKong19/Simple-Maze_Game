import pytest
from views.maze_view import MazeView

@pytest.fixture()
def test_maze():
    return MazeView('Maze','Maze')

def test_maze_view(test_maze):
    """
    Check the class has the correct attributes
    """
    assert hasattr(test_maze, 'maze')
    assert hasattr(test_maze, '_name')
    assert hasattr(test_maze, 'start_time')
    assert hasattr(test_maze, 'timer')
    assert hasattr(test_maze,'display_maze')

def test_display(test_maze):
    """
    Checks to see if Maze has a display attribute
    """
    assert hasattr(test_maze,'display')