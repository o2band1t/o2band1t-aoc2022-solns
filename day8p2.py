with open('day8_input.txt', 'r') as f:
	raw = [l.replace('\n', '') for l in f.readlines()]

grid = [[int(n) for n in l] for l in raw]
end = len(grid) - 1

max_view = 0

for row in range(end + 1):
	for col in range(end + 1):
		n, s, e, w = 0, 0, 0, 0
		ht = grid[row][col]
		for c in range(1, col + 1):
			w += 1
			if grid[row][col - c] >= ht: break
		for c in range(col, end + 1):
			if c == col: continue
			e += 1
			if grid[row][c] >= ht: break
		for r in range(1, row + 1):
			n += 1
			if grid[row - r][col] >= ht: break
		for r in range(row, end + 1):
			if r == row: continue
			s += 1
			if grid[r][col] >= ht: break
		score = n * s * e * w
		if score > max_view:
			max_view = score

print(max_view)
