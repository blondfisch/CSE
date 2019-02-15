class SuperBowl(object):
    def __init__(self, sadness="sadness", team_one_score=0, team_two_score=0):
        self.sadness = sadness
        self.enjoyment = False
        self.team_one_score = team_one_score
        self.team_two_score = team_two_score
        self.halftime = "Maroon Five"
        self.playing = True

    def _update_score(self):
        print("The score is {}:{}.".format(self.team_one_score, self.team_two_score))

    def score_change(self, team):
        if team == "one":
            points = int(input("How many points were scored?"))
            self.team_one_score += points
            self._update_score()
        if team == "two":
            points = int(input("How many points were scored?"))
            self.team_two_score += points
            self._update_score()
        elif team != "one" and team != "two":
            print("Because I fell asleep, I couldn't tell who scored. Type one or two next time and maybe I'll care.")

    def performer_change(self, performer):
        self.halftime = performer
        print("Now {} is performing. It still sucks that they won't play Sweet Victory.".format(self.halftime))

    def enjoy(self):
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


jac = SuperBowl("rage")
jac.feeling(jac)
jac.score_change("one")
