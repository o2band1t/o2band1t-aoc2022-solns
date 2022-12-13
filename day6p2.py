from collections import deque

with open('day6_input.txt', 'r') as f:
	raw = f.read()

past_fourteen = deque()

for i, c in enumerate(raw, start=1):
	found = True
	past_fourteen.append(c)
	if len(past_fourteen) > 14:
		past_fourteen.popleft()
		for elem in past_fourteen:
			if past_fourteen.count(elem) > 1:
				found = False
				break
		if found:
			print(i, past_fourteen, elem)
			break
