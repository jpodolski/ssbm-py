## @file player.py
## @author Jeff Podolski
## @todo
#   - Perhaps add a hash function to give each player a unique ID
#   - Write a create-from-json-data initializaer
#   - Make more comprehensive (region, rank, mains, etc)

# ==============================================================================
"""

PLAYER.PY

Attribution 4.0 International (CC BY 4.0)

All code below is free and open source, intended to better the smash community
You are free to copy, modify, and redistribute this code as long as credit
is given to the original author (Jeff Podolski). Check out the source!

Github Repo: http://github.com/jpodolski/ssbm-py
Sharing License: https://creativecommons.org/licenses/by/4.0/

"""
# ==============================================================================

from information import *

class Player:
    """
    A class describing a specific player.
    Used by Match, Tournament, and possible future
    stat-keeping applications
    """

    #  Initialization
    #  ==============================
    def __init__(self):
        self.__tag = 'player_tag'
        self.__port = 0
        self.__prefix = 'player_sponsor'
        self.__char = 'Generic'
        self.__sub_color = 0 # Not comparable to team
        self.__team = 0 # 0 = None, 1 = Red, 2 = Blue, 3 = Green

    #  Mutators
    #  ==============================
    def set_tag(self, new_tag):
        """ A mutator for __tag """
        self.__tag = new_tag

    def set_port(self, new_port):
        """ A mutator for __port """
        self.__port = new_port

    def set_prefox(self, new_prefix):
        """ A mutator for __prefix """
        self.__prefix = new_prefix

    def set_char(self, new_char):
        """ A mutator for __char """
        self.__char = new_char

    def set_sub_color(self, new_sub_color):
        """ A mutator for __sub_color """
        self.__sub_color = new_sub_color%(char_mod_table[character_names.index(self.__char)])

    def set_team(self, new_team):
        """ A mutator for __team """
        self.__team = new_team

    #  Accessors
    #  ==============================
    def get_tag(self):
        """ An accessor for __tag """
        return self.__tag
    def get_port(self):
        """ An accessor for __port """
        return self.__port
    def get_prefix(self):
        """ An accessor for __prefix """
        return self.__prefix
    def get_char(self):
        """ An accessor for __char """
        return self.__char
    def get_sub_color(self):
        """ An accessor for __sub_color """
        return self.__sub_color
    def get_team(self):
        """ An accessor for __team """
        return self.__team
