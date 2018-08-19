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

# All characters that can be played in SSBM
character_names = []
character_names.append("")
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

team_colors = ["", "Red Team", "Blue Team", "Green Team"]

""" How many costumes does each character have? """
char_mod_table = [
	0, 3, 3, 4, 4, 4, 4,
	5, 3, 4, 3, 3, 5, 4,
	4, 4, 4, 4, 4, 3, 4,
	3, 4, 3, 3, 3, 5, 0
	]



""" a list of esports teams (currently unused)"""
teams = ["100thieves",
		 "adfinem",
		 "ago",
		 "ahq",
		 "alliance",
		 "avangar",
		 "bausupermassive",
		 "big",
		 "binarydragons",
		 "boot",
		 "bravado",
		 "cg",
		 "chiefs",
		 "clg",
		 "cloud9",
		 "complexity",
		 "darkpassage",
		 "digitalchaos",
		 "dignitas",
		 "direwolves",
		 "edg",
		 "effect",
		 "eg",
		 "ehome",
		 "empire",
		 "envy",
		 "execration",
		 "faze",
		 "fenerbahce",
		 "flashgaming",
		 "flashwolves",
		 "flipsid3",
		 "fnatic",
		 "galeforce",
		 "gambit",
		 "giants",
		 "godsent",
		 "h2k",
		 "happyfeet",
		 "hellraiser",
		 "heroic",
		 "hkes",
		 "immortals",
		 "infamous",
		 "invictus",
		 "isurus",
		 "jteam",
		 "keen",
		 "kinguin",
		 "kongdoomonster",
		 "kpi",
		 "ldlc",
		 "lfy",
		 "lgd",
		 "longzhu",
		 "luminosity",
		 "lyon",
		 "m19",
		 "marines",
		 "max",
		 "mineski",
		 "misfits",
		 "mongolz",
		 "mouse",
		 "mvp",
		 "navi",
		 "newbee",
		 "north",
		 "np",
		 "nrg",
		 "optic",
		 "order",
		 "pain",
		 "penta",
		 "phoenix",
		 "planetdog",
		 "pyjamas",
		 "quantum",
		 "rampage",
		 "redbullog",
		 "redcanids",
		 "redreserve",
		 "renegades",
		 "risenation",
		 "rng",
		 "rogue",
		 "roxtigers",
		 "secret",
		 "sg",
		 "singularity",
		 "sktelecom",
		 "spacesoldiers",
		 "sprout",
		 "tempostorm",
		 "tnc",
		 "torqued",
		 "tricked",
		 "tsm",
		 "tyloo",
		 "unicornsoflove",
		 "vegasquad",
		 "vgjthunder",
		 "vici",
		 "virtus",
		 "vitality",
		 "we",
		 "wgunity",
		 "wings",
		 "wololos"]