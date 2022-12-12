with open('day4_input.txt', 'r') as f:
	raw = [l.replace('\n', '').split(',') for l in f.readlines()]

pairs = 0

for l in raw:
	r0 = tuple(map(int, l[0].split('-')))
	r1 = tuple(map(int, l[1].split('-')))
	if (r0[0] <= r1[0]) and (r0[1] >= r1[0]) \
	or (r1[0] <= r0[0]) and (r1[1] >= r0[0]):
		pairs += 1

print(pairs)
