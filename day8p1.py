with open('day8_input.txt', 'r') as f:
	raw = [l.replace('\n', '') for l in f.readlines()]

grid = [[int(n) for n in l] for l in raw]
end = len(grid) - 1
vis = set()

row = 0
while row <= end:
	left_max, right_max = -1, -1
	col_left, col_right = 0, end
	while col_left <= end and col_right >= 0:
		if grid[row][col_left] > left_max:
			left_max = grid[row][col_left]
			vis.add((row, col_left))
		if grid[row][col_right] > right_max:
			right_max = grid[row][col_right]
			vis.add((row, col_right))
		col_left += 1
		col_right -= 1
	row += 1

col = 0
while col <= end:
	top_max, bottom_max = -1, -1
	row_top, row_bottom = 0, end
	while row_top <= end and row_bottom >= 0:
		if grid[row_top][col] > top_max:
			top_max = grid[row_top][col]
			vis.add((row_top, col))
		if grid[row_bottom][col] > bottom_max:
			bottom_max = grid[row_bottom][col]
			vis.add((row_bottom, col))
		row_top += 1
		row_bottom -= 1
	col += 1

print(len(vis))
