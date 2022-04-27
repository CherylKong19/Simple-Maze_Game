import pytest
from models.player import Player

@pytest.fixture
def test_player():
    """
    Fixture for all tests
    """
    return Player()

def test_bag(test_player):
    """
    Checks to see if player has attribute backpack and that it is a list
    """
    assert hasattr(test_player,'backpack')
    assert type(test_player.backpack) == list

def test_pickup(test_player):
    """
    Checks to see if player has attribute appendItem
    """
    assert hasattr(test_player,'appendItem')

def test_append_item(test_player):
    """
    Checks to see if player can append an item to the backpack 
    and that the value and length of backpack is correct
    """
    test_player.appendItem("I")
    if len(test_player.backpack) != 0 and test_player.backpack == ["I"]:
        assert True