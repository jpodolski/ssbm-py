# ========== DOXYGEN ==========
## @file match.py
## @author Jeff Podolski

from player import Player

## The Match class is designed to be a basic class that holds essential information about a set.
# it contains information on the players in the match in the form of four Player objects, labeled 1-4
# note that regardless of the notation in the code, any player can be assigned to any port. Players are accessed
# by accessor functions, for example (what_team = winners_semis.p1.get_team())
class Match:
	def __init__(self):
		self.p1 = Player()
		self.p2 = Player()
		self.p3 = Player()
		self.p4 = Player()
		self.__bestOf = 3
		self.__singles = 1
		self.__round = "Friendlies"
	def is_singles(self):
		return (self.__singles == 1)
	def get_best_of(self):
		return(self.__bestOf)
	def get_set_round(self, roundString):
		self.__round = roundString


