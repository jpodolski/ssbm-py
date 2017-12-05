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
character_names = []
character_names.append("Fox")
character_names.append("Falco")
character_names.append("Marth")
character_names.append("Sheik")
character_names.append("Jigglypuff")
character_names.append("Peach")
character_names.append("Captain Falcon")
character_names.append("Ice Climbers")
character_names.append("Samus")
character_names.append("Pikachu")
character_names.append("Luigi")
character_names.append("Yoshi")
character_names.append("Doctor Mario")
character_names.append("Ganondorf")
character_names.append("Mario")
character_names.append("Young Link")
character_names.append("Link")
character_names.append("Donkey Kong")
character_names.append("Mr. Game & Watch")
character_names.append("Roy")
character_names.append("Mewtwo")
character_names.append("Zelda")
character_names.append("Pichu")
character_names.append("Ness")
character_names.append("Bowser")
character_names.append("Kirby")
character_names.append("Generic")
ports = ["Player 1", "Player 2", "Player 3", "Player 4"]
char_mod_table = [3, 3, 4, 4, 4, 4, 5, 3, 4, 3, 3, 5, 4, 4, 4, 4, 4, 4, 3, 4, 3, 4, 3, 3, 3, 5, 0]
