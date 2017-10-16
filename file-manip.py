def new_match():
	match = {
		'singles': 1,
		'set-len': 3,
		
		'player-a': 'Player A',
		'player-b': 'Player B',
		'player-c': 'Player C',
		'player-d': 'Player D',
		
		'pA-port': 1,
		'pB-port': 2,
		'pC-port': 3,
		'pD-port': 4,
		
		'pA-team': 0,
		'pB-team': 0,
		'pC-team': 1,
		'pD-team': 1}
	return match

def print_ports(match):
	print(match['pA-port'])
	print(match['pB-port'])
	print(match['pC-port'])
	print(match['pD-port'])

my_match = new_match()

my_match['pC-port'] = 2
my_match['pA-port'] = 3
my_match['pD-port'] = 1
my_match['pB-port'] = 4

print_ports(my_match)


