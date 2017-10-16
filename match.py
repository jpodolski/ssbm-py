class Match:
#	singles = 1
#	length = 3
	playerA = 'Player A'
	playerB = 'Player B'
	playerC = 'Player C'
	playerD = 'Player D'
	pAport = 1
	pBport = 2
	pCport = 3
	pDport = 4
#	pATeam = 0
#	pBTeam = 0
#	pCTeam = 1
#	pDTeam = 1
	def __init__(self):
		self.pAport = 1
		self.pBport = 2
		self.pCport = 3
		self.pDport = 4

	def print_ports(self):
		print(self.pAport)
		print(self.pBport)
	def set_ports(self, a=0, b=0, c=0, d=0):
		self.pAport = a
		self.pBport = b
		self.pCport = c
		self.pDport = d
	def set_tagA(self, name_A):
		self.playerA = name_A
	def set_tagB(self, name_B):
		self.platerB = name_B

def print_hey():
	print("HEY")
