This is a simple Maze game created with Pygame and Flask. It is done as a group project for ACIT2515-Object Oriented Programming in Python.

# Dependencies
------------------------
- Pygame
- Flask
- Pytest

# Set Up Environment and Install Dependencies
------------------------
1. In Powershell or any terminal, create a virtual environment if you do not have one and activate the virtual environment.
    Powershell:
    To create a virtual environment: ```py -m venv <name>```
    To activate the virtual environment: ```.\<name>\Scripts\activate.ps1```
2. Run ```pip install -r requirements.txt```

# How to Run the game
------------------------
1. Go to the maze directory. 
2. Run main.py in the maze folder.
3. Enter your name before you start the game.

Now, you can start playing the game.

## How to control the game
------------------------
- 'W' key is up
- 'S' key is down
- 'A' key is left
- 'D' key is right
- 'X' key is exit the game

## How to win the game
------------------------
1. Collect all the items and reach to the Exit within a given time

Exceptions:
You will lose the game if you do not collect all the items before you reach the exit, 
or you do not reach the exit wihtin a given time.

# How to run the Flask application
----------------------------------
1. Go to web directory
2. Run app.py
3. Copy the url and open it in your web browser.
4. You will then see a score rank from highest to lowest if you have played the game at least one time.
5. You can modify scores with different urls.

## Summary of our Web API
------------------------
### URL: /
- Display a list of score rank sorting highest to lowest. 
- Mehtod: GET

### URL: /api/list 
- Method: POST
- Comments: JSON must be a dictionary with name of the user available in name key.
- If the name is in our database, it will be removed from the score rank and our database.
- Status code: 204(empty response) or 400(invalid values from client)

### URL: /api/new
- Method: PUT
- Comments: JSON must be a dictionary with name and score of the key have valid values.
- Add a new score to manager.
- Status code: 204(empty response) or 400(invalid values from client)

### URL: /api/list
- Return JSON dictionary: {"score": [list of all scores]}
- Mehtod: GET
- Status code: 200

# To run unit test
-----------------

## To test the maze game
-------------------
1. Go to maze/test directory
2. Run 'pytest' in command line
3. You will see results in all test files that being found and test in that directory.

## To test the app
-------------------
1. Go to the web directory
2. Run 'pytest' in command line
3. You will see the result of the app test.