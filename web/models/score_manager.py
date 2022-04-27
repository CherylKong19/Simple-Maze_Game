from .score import Score
import json

class ScoreManager:
    """Class that collects and manages scores
    """

    def __init__(self):
        """Creates an instance of ScoreManager with an empty dictionary 
        """
        self._scores = {}

    @property
    def scores(self):
        """Returns a list of Scores from the ScoreManager dictionary

        :return: list of objects
        :rtype: list
        """
        return list(self._scores.values())

    def add_score(self, add):
        """Adds an instance of Score to the ScoreManager

        :param add: instance of Score
        :type add: object
        """
        self._scores[add.name] = add

    def remove_score(self, remove):
        """Removes an instance of Score from the ScoreManager

        :param remove: intance of Score
        :type remove: String
        """
        self._scores.pop(remove)

    def __len__(self):
        """Returns the length of the ScoreManager dictionary

        :return: length of dictionary
        :rtype: int
        """
        return len(self._scores)

    def get_scores(self):
        """Creates a list of dictionary entries of scores 

        :return: list of dictionaries
        :rtype: list
        """
        all_scores = []
        for i in self.scores:
            score_dict = i.to_dict()
            all_scores.append(score_dict)
        return all_scores

    def serialize(self):
        """Returns a dictionary version of a set of scores

        :return: dictionary of scores
        :rtype: dictionary
        """
        serial = {}
        serial["scores"] = self.get_scores()
        return serial

    def to_json(self, json_file):
        """Dumps to a json file

        :param json_file: A json file
        :type json_file: json file
        """
        with open(json_file, "w") as outfile:
            json.dump(self.serialize(), outfile)

    def from_json(self, json_file):
        """Reads from a json file

        :param json_file: a json file
        :type json_file: json file
        """
        with open(json_file, "r") as loadfile:
            data = json.load(loadfile)
            for item in data.get("scores"):
                new_score = Score(item.get("name"), item.get("score"), item.get("date"))
                self.add_score(new_score)