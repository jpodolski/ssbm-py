#            \\======\\  DOXYGEN //======//

## @file match.py
## @author Jeff Podolski
## @todo
#   - Make these storable and serializable
#   - Have a table of possible rounds (GF2, Pools, WSF, etc.)
#   - Make more comprehensive (date, tournament, etc)

# ==============================================================================
"""
             \\======\\  INFO //======//

Match.py

Copyright (C) 2017 Jeff Podolski <jpodolski@protonmail.com>
Attribution 4.0 International (CC BY 4.0)

All code below is free and open source, intended to better the smash community
You are free to copy, modify, and redistribute this code as long as credit
is given to the original author (Jeff Podolski). Check out the source!

Github Repo: http://github.com/jpodolski/ssbm-py
Sharing License: https://creativecommons.org/licenses/by/4.0/

"""
# ==============================================================================

from player import Player

class Match(object): # pylint: disable=too-few-public-methods
    """
    The Match class is designed to be a basic class that
    holds essential information about a set. And can be modified
    it contains information on the players in the match
    in the form of four Player objects, labeled 1-4
    note that regardless of the notation in the code,
    any player can be assigned to any port. Players are accessed
    by their respective accessor functions.
    """
    def __init__(self):
        self.player = []
        for i in range(0, 4):
            player_object = Player()
            self.player.append(player_object)
        self.__best_of = 3
        self.__singles = 1
        self.__round = "Friendlies"
    def is_singles(self):
        """ Returns True if the match is a singles match """
        return self.__singles == 1
    def get_best_of(self):
        """ Return the total number of games (e.g., Bo3 == 3)"""
        return self.__best_of
    def get_set_round(self, round_string):
        """ Returns a string"""
        self.__round = round_string
