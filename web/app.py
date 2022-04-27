from flask import Flask, request, render_template
from models.score import Score
from models.score_manager import ScoreManager
import os

#create the web app
app = Flask(__name__)
score_manager = ScoreManager()
try:
    #get scores from json file
    score_manager.from_json("../scores.json")
except FileNotFoundError:
    print('You have not play any game, so the score rank will be empty. Please play our game and come back!')

@app.route('/api/list')
def list_all_scores():
    """
    Display all score in from of list
    """
    return {"scores": score_manager.get_scores()}

@app.route('/api/new', methods=["PUT"])
def add_new_score():
    """
    Create a new score instnace adn add into score rank
    """
    try:
    #-- get the JSON data of the request, containing a new object to add        
        data = request.get_json()
        if ("name" in data) and ("score" in data):
            new_score = Score(data["name"], data["score"], data["date"])
            score_manager.add_score(new_score)
            return"", 204 
        else:
            return"Invalid data provided.", 400
    except:
        return"Invalid data provided.", 400

@app.route('/api/list', methods=["POST"])
def delete_score():
    """
    Remove teh screo from databse and score rank
    """
    try:
        #-- get the JSON data of the request, containing an object to remove       
        data = request.get_json()
        name = "name"
        delete = []

        if name in data:
            for key in score_manager._scores.keys():

                if key == data["name"]:
                    delete.append(key)

            for i in delete:
                del score_manager._scores[i]

        return"", 204 

    except:
        return"Invalid data provided.", 400

@app.route('/')
def list_all_scores_html():
    """
    Displays the scores in order from highest to lower in an html webpage
    """
    scores = score_manager.get_scores()
    sorted_scores = []
    for count, item in enumerate(scores):
        next_score = item
        for count2, item2 in enumerate(scores):
            if (item2.get("score")) > (next_score.get("score")):
                next_score = item2
                count = count2
        scores.pop(count)
        sorted_scores.append(next_score)
    full_sort = sorted_scores + scores
    if len(full_sort) == 0:
        return render_template("empty_list.html")

    return render_template("list.html", scores=full_sort)

if __name__ == "__main__":
    print("main")
    app.run(debug=True)
