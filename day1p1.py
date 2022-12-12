with open('day1_input.txt', 'r') as f:
	raw = f.readlines()

elves = [0]

for line in raw:
	try:
		elves[len(elves)-1] += int(line)
	except ValueError:
		elves.append(0)

biggest_weight = 0
most_elf = 0

for elf in enumerate(elves, start=1):
	if elf[1] > biggest_weight:
		biggest_weight = elf[1]
		most_elf = elf[0]

print(most_elf, biggest_weight)
print(len(elves))
