with open('day3_input.txt', 'r') as f:
	raw = [l.replace('\n', '') for l in f.readlines()]

abc = 'abcdefghijklmnopqrstuvwxyz'
priority = {k:p for p, k in enumerate(abc + abc.upper(), start=1)}

print(priority)

type_sum = 0

for l in raw:
	ruck = l
	ruck1 = ruck[:int(len(ruck)/2)]
	ruck2 = ruck[int(len(ruck)/2):]
	for item in ruck1:
		if item in ruck2:
			type_sum += priority[item]
			break

print(type_sum)
