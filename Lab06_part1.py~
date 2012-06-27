"""
Lab_Python_06
Part 1
"""

import datetime

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/22/2012	| 1
"""
import datetime
## create the player_stats data structure
"""player={'6/23/2012':('rooney',2), \
        '6/25/2012':('rooney',2), \
        '6/19/2012':('ronaldo',0), \
        '6/20/2012':('ronaldo',3), \
        '6/21/2012':('torres',0), \
        '6/22/2012':('torres',1)}
print 'Players ', player
"""
player_stats={'rooney':[[datetime.date(2012,6,23),\
                   datetime.date(2012,6,25)],[2,2]],\
        'ronaldo':[[datetime.date(2012,6,19),\
                    datetime.date(2012,6,20)],[0,3]],\
        'torres': [[datetime.date(2012,6,21),\
                    datetime.date(2012,6,22)],[0,1]]}

print 'Players ', player_stats['rooney'][0][0]
## implement highest_score
"""highest=0
for p in player:
    if highest<player[p][1]:
        highest=player[p][1]
print 'highest score', highest
"""
def highest_score(player_stats):
    highest=0
    theplayer=""
    thedate=""
    for p in player_stats:
        #print player_stats[p][1][0]
        if highest< player_stats[p][1][0]:
            highest=player_stats[p][1][0]
            theplayer=p
            thedate=player_stats[p][0][0]
        if highest< player_stats[p][1][1]:
            highest=player_stats[p][1][1]
            theplayer=p
            thedate=player_stats[p][0][1]
    return (theplayer,thedate,highest)
print highest_score(player_stats)
## implement highest_score_for_player
def highest_score_for_player(player_stats,player):
    highest=0
    i=-1
    for score in player_stats[player][1]:
        i+=1
        # print i," ",score
        if highest< score:
            highest=score
            thedate=player_stats[player][0][i]
    return (player,thedate,highest)

player='torres'
print player+ "'s ",\
highest_score_for_player(player_stats,player)

## implement highest_scorer
def highest_scorer(player_stats):
    highest=0
    theplayer=""
    for p in player_stats:
        add=player_stats[p][1][0]+player_stats[p][1][1] 
        if highest< add:
            highest=add
            theplayer=p
    return theplayer
print 'the Player is ',highest_scorer(player_stats)








<<<<<<< HEAD




=======
## implement highest_score


## implement highest_score_for_player
>>>>>>> dd6c931fd69fd574dea64e7ef796d56adad263a6



