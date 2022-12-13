from collections import deque

with open('day6_input.txt', 'r') as f:
	raw = f.read()

past_four = deque()

for i, c in enumerate(raw, start=1):
	found = True
	past_four.append(c)
	if len(past_four) > 4:
		past_four.popleft()
		for elem in past_four:
			if past_four.count(elem) > 1:
				found = False
				break
		if found:
			print(i, past_four, elem)
			break
