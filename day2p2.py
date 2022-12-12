with open('day2_input.txt', 'r') as f:
	raw = [l.replace('\n', '').split(' ') for l in f.readlines()]

win = {
	'A': 'paper',
	'B': 'scissors',
	'C': 'rock'
}

draw = {
	'A': 'rock',
	'B': 'paper',
	'C': 'scissors'
}

lose = {
	'A': 'scissors',
	'B': 'rock',
	'C': 'paper'
}

pts = {
	'rock': 1,
	'paper': 2,
	'scissors': 3
}

outcome = {
	'X': 0,
	'Y': 3,
	'Z': 6
}

score = 0

for opp_move, result in raw:	
	score += outcome[result]
	if result == 'X':
		score += pts[lose[opp_move]]
	elif result == 'Y':
		score += pts[draw[opp_move]]
	else:
		score += pts[win[opp_move]]

print(score)
