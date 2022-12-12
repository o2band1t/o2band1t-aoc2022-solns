with open('day5_input.txt', 'r') as f:
	raw = [l.replace('\n', '') for l in f.readlines()]

stacks = {
	1: list('LNWTD'),
	2: list('CPH'),
	3: list('WPHNDGMJ'),
	4: list('CWSNTQL'),
	5: list('PHCN'),
	6: list('THNDMWQB'),
	7: list('MBRJGSL'),
	8: list('ZNWGVBRT'),
	9: list('WGDNPL')
}

message = ''

for l in raw:
	for w in ('move', 'from', 'to'):
		l = l.replace(w, '')
	move, from_, to = [int(n) for n in l.split(' ') if n != '']
	stacks[to] += stacks[from_][-move:]
	stacks[from_] = stacks[from_][:-move]

for s in stacks.values():
	message += s.pop()

print(message)
