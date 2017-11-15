## @file information.py
## @author Jeff Podolski
## @todo
#   - Perhaps add a hash function to give each player a unique ID
#   - Write a create-from-json-data initializaer
#   - Make more comprehensive (region, rank, mains, etc)

# ==============================================================================
"""

INFORMATION.PY

Attribution 4.0 International (CC BY 4.0)

All code below is free and open source, intended to better the smash community
You are free to copy, modify, and redistribute this code as long as credit
is given to the original author (Jeff Podolski). Check out the source!

Github Repo: http://github.com/jpodolski/ssbm-py
Sharing License: https://creativecommons.org/licenses/by/4.0/

"""
# ==============================================================================

# All characters that can be played with in SSBM
character_names = [
	"Fox",
	"Falco",
	"Marth",
	"Sheik",
	"Jigglypuff",
	"Peach",
	"Captain Falcon",
	"Ice Climbers",
	"Samus",
	"Pikachu",
	"Luigi",
	"Yoshi",
	"Doctor Mario",
	"Ganondorf",
	"Mario",
	"Young Link",
	"Link",
	"Donkey Kong",
	"Mr. Game & Watch",
	"Roy",
	"Mewtwo",
	"Zelda",
	"Pichu",
	"Ness",
	"Bowser",
	"Kirby",
	"Generic"
]


ports = [
	"Player 1",
	"Player 2",
	"Player 3",
	"Player 4"
]

char_mod_table = [3, 3, 4, 4, 4, 4, 5, 3, 4, 3, 3, 5, 4, 4, 4, 4, 4, 4, 3, 4, 3, 4, 3, 3, 3, 5, 0]
