import pytest
import json
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_get_list(client):
    """
    Test if the app can get the correct format of list of scores.
    thr format should be {"scores": []}
    """
    req = client.get("/api/list")
    text_contents = req.data.decode()
    assert json.loads(text_contents) == {"scores": []}

def test_put_new(client):
    """
    Test if it can createt a new Score instamce and add into the score rank
    """
    req = client.put("/api/new", json={"name": "Test", "score": 100, "date": "10:44:38.491000"})
    assert req.status_code == 204

    #Check if the list has appended the new score
    req = client.get("/api/list")
    assert req.get_json() == {"scores": [{"name": "Test", "score": 100, "date": "10:44:38.491000"}]}

    #Check the status code will be 400 when invlaid input are received
    req = client.put("/api/new", json={"name": "invalid"})
    assert req.status_code == 400

    req = client.put("/api/new")
    assert req.status_code == 400

def test_delete_list(client):
    """
    Test if it can delete a Score instamce and remove into the score rank
    """
    #Create a new score instance
    client.put("/api/new", json={"name": "Test", "score": 100})

    req = client.post("/api/list", json={"name": "Test"})
    assert req.status_code == 204
    
    #Check if the list has removed the new score
    req = client.get("/api/list")
    assert req.get_json() == {"scores": []}

    #check status code to be 400 when no arguement is received
    req = client.post("/api/list")
    assert req.status_code == 400