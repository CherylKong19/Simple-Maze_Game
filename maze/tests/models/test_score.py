import pytest
from models.score import Score

@pytest.fixture
def high():
    return Score("Albert", 0, '10:43:29.392756')

@pytest.fixture
def low():
    return Score("Barry", 999, '10:44:38.491000')

def test_change_name(high):
    """
    Check the calss name attribute has the correct value
    """
    high.name = 'Alb'
    assert high.name == 'Alb'

def test_change_score(high):
    """
    Check the calss score attribute has the correct value
    """
    high._score = 998
    assert high.score == 998

def test_change_date(high):
    """
    Check the calss date attribute has the correct value
    """
    high._date = '10:44:38.491045'
    assert high.date == '10:44:38.491045'

def test_score_to_dict(low):
    """
    Check the function to add the correct score in dictionary
    """
    assert low.to_dict() == {"name": "Barry", "score": 999, "date": '10:44:38.491000'}