import datetime
#1
class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name = firstname
        self.last_name = lastname
        self.scores = []
        self.team = team   
    #2
    def add_score(self,date,score):
        self.scores.append(score)
    #3
    def total_score(self):
        return sum(self.scores)

    def average_score(self):
        result=float(sum(self.scores))/len(self.scores)
        return result
    
    def print_score(self):
        print  self.scores
        
class Team:
    def __init__(self,Name):
        self.name=Name
        self.league=""
        self.manager_name=""
        self.points=0
        self.players=[]

    def add_player(self,player):
        self.players.append(player)

    def __str__(self):
        return self.name


class Match:
    def __init__(self,hometeam,awayteam,date):
        self.home_team=hometeam
        self.away_team=awayteam
        self.date=date
        self.home_scores={}
        self.away_scores={}

    def home_score(self):
        return sum(self.home_scores.values())

    def away_score(self):
        return sum(self.away_scores.values())

    def winner(self):
        if self.home_score() > self.away_score():
            print 'Winner!!! ',
            return self.home_team.name
        elif self.home_score() < self.away_score():
            print 'Winner!!! ',
            return self.away_team.name
        else:
            return 'Draw'

    def add_score(self,player,score):
        theteam=player.team
        if theteam==self.home_team:
            print 'home team'
            if player.last_name in self.home_scores.keys():
                self.home_scores[player.last_name]+=score
            else:
                self.home_scores[player.last_name]=score
        if theteam==self.away_team:
            print 'away team'
            if player.last_name in self.away_scores.keys():
                self.away_scores[player.last_name]+=score
            else:
                self.away_scores[player.last_name]=score
            



torres=Player('Fernando','Torres','chelsea')
for score in [0,0,1,0,1]:
    torres.add_score(datetime.date(2000,1,1),score)

print "Torres' average score ",torres.average_score()

spain=Team('Spain')
portugal=Team('Portugal')

torres=Player('Fernando','Torres',spain)
ronaldo=Player('Christiano','Ronaldo',portugal)

spain.add_player(torres)
portugal.add_player(ronaldo)

print 'printing team ', spain


euro_semi_final=Match(spain,portugal,datetime.date(2012,6,27))
euro_semi_final.add_score(torres,1)    
euro_semi_final.add_score(ronaldo,5)
euro_semi_final.add_score(torres,1)

print euro_semi_final.winner()











        






        
