with open('day1_input.txt', 'r') as f:
	raw = f.readlines()

elves = [0]

for line in raw:
	try:
		elves[len(elves)-1] += int(line)
	except ValueError:
		elves.append(0)

print(sum(sorted(elves, reverse=True)[:3]))

