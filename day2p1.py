with open('day2_input.txt', 'r') as f:
	raw = [l.replace('\n', '').split(' ') for l in f.readlines()]

win = {
	'A': 'Y',
	'B': 'Z',
	'C': 'X'
}

draw = {
	'A': 'X',
	'B': 'Y',
	'C': 'Z'
}

pts = {
	'X': 1,		# rock
	'Y': 2,		# paper
	'Z': 3		# scissors
}

score = 0

for game in raw:
	score += pts[game[1]]
	if win[game[0]] == game[1]:
		score += 6
	elif draw[game[0]] == game[1]:
		score += 3

print(score)
