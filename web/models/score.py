import datetime, json

class Score:
    """An object that houses a name, score, and date to be exported

    :return: Score object
    :rtype: object
    """

    current = datetime.datetime.now()

    def __init__(self, _name="", _score=0, _date="Date: {}, Time: {}".format(current.date(), current.time())):
        """Creates the score object

        :param _name: A player's name, defaults to ""
        :type _name: str, optional
        :param _score: A score between 0 and 100, defaults to 0
        :type _score: int, optional
        :param _date: A string representing the date, defaults to "Date: {}, Time: {}".format(current.date(), current.time())
        :type _date: string, optional
        """
        self._player_name = _name
        self._score = _score
        self._date = _date

    @property
    def change_name(self, name):
        """Changes the player name

        :param name: new name
        :type name: string
        """
        self._player_name = name

    @property
    def change_score(self, score):
        """Changes the player score

        :param score: new score
        :type score: int
        """
        self._score = score

    @property
    def change_date(self, date):
        """Changes the date

        :param date: new date
        :type date: string
        """
        self._date = date

    @property
    def name(self):
        """Returns name

        :return: player name
        :rtype: string
        """
        return self._player_name

    @property
    def score(self):
        """Returns score

        :return: player score
        :rtype: int
        """
        return self._score

    @property
    def date(self):
        """Returns the date

        :return: score date
        :rtype: string
        """
        return self._date

    def to_dict(self):
        """Changes a score object into a dictionary

        :return: score as a dictionary
        :rtype: dictionary
        """
        score_dict = {}
        score_dict["name"] = self.name
        score_dict["score"] = self.score
        score_dict["date"] = self.date
        return score_dict