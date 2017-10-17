# ========== DOXYGEN ==========
## @file player.py
## @author Jeff Podolski

class Player:
		def __init__(self):
			self.__tag = 'player_tag'
			self.__port = 0
			self.__sponsor = 'player_sponsor'
			self.__char = 'Generic'
			self.__sub_color = 0 # Not comparable to team
			self.__team = 0 # 0 = None, 1 = Red, 2 = Blue, 3 = Green

		def set_tag(self, new_tag):
			self.__tag = new_tag
		def set_port(self, new_port):
			self.__port = new_port
		def set_sponsor(self, new_sponsor):
			self.__sponsor = new_sponsor
		def set_char(self, new_char):
			self.__char = new_char
		def set_sub_color(self, new_sub_color):
			self.__sub_color = new_sub_color
		def set_team(self, new_team):
			self.__team = new_team

		def get_tag(self):
			return(self.__tag)	
		def get_port(self):
			return(self.__port)		
		def get_sponsor(self):
			return(self.__sponsor)	
		def get_char(self):
			return(self.__char)	
		def get_sub_color(self):
			return(self.__sub_color)	
		def get_team(self):
			return(self.__team)