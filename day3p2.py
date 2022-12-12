with open('day3_input.txt', 'r') as f:
	raw = [l.replace('\n', '') for l in f.readlines()]

abc = 'abcdefghijklmnopqrstuvwxyz'
priority = {k:p for p, k in enumerate(abc + abc.upper(), start=1)}

type_sum = 0

groups = [raw[i-2:i+1] for i in range(2, len(raw), 3)]
for g in groups:
	type_sum += priority[
		list(
			set(g[0]).intersection(
				set(g[1]).intersection(
					set(g[2])
				)
			)
		)[0]
	]

print(type_sum)
