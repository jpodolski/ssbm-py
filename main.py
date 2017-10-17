import glob
import os
from match import Match
from player import Player

my_match = Match()

print(my_match.p1.get_tag())
my_match.p1.set_tag("Helo")
print(my_match.p1.get_tag())