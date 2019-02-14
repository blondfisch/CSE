import random


class SuperBowl(object):
    def __init__(self, sadness, team_one_score=0, team_two_score=0, stress_eating="too much"):
        self.sadness = sadness
        self.gifts = stress_eating
        self.enjoyment = False
        self.team_one_score = team_one_score
        self.team_two_score = team_two_score
        self.score = str(team_one_score) + ":" + str(team_two_score)
        self.halftime = "Maroon Five"
        self.playing = True

    def score_change(self, team, points):
        if team == "one":
            self.team_one_score += points
        if team == "two":
            self.team_two_score += points
        else:
            print("Because I fell asleep, I couldn't tell who scored. Type one or two next time and maybe I'll care.")
        print(self.score)

    def performer_change(self, performer):
        self.halftime = performer
        print("Now {} is performing. It still sucks that they won't play Sweet Victory.".format(self.halftime))

    def enjoyment(self):
        if self.enjoyment is False:
            print("Did something happen? Didn't think so. Go cry in a corner.")
        else:
            print("You are absolutely insane if you think this is entertaining.")

    def game_over(self):
        self.playing = False
        print("Thank Weibeus that it is finally over.")

    @staticmethod
    def feeling(self):
        print("All I feel is {}".format(self.sadness))


jac = SuperBowl("sadness", 0, 0)
jac.enjoyment()
