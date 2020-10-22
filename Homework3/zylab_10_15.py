# Luis Onate
# 1596900

# class representing information about a food item
class Team:
    def __init__(self, team_name='None', team_wins=0, team_losses=0):
        self.team_name = team_name
        self.team_wins = team_wins
        self.team_losses = team_losses

    # definition that's used for calculating the percentage of wins and losses
    def get_win_percentage(self):
        percent = float(self.team_wins / (self.team_wins + self.team_losses))
        return percent


# unit testing
if __name__ == '__main__':
    name = Team(input(), int(input()), int(input()))  # call to Team class with user inputs for parameters

    # if-else statement used to check whether result of calculation is over .5 or below .5
    if name.get_win_percentage() >= 0.5:  # if over .5 the following is printed
        print('Congratulations, Team {} has a winning average!'.format(name.team_name))
    else:  # else prints the following
        print('Team {} has a losing average.'.format(name.team_name))
