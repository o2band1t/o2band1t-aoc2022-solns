with open('day7_input.txt', 'r') as f:
	raw = [l.replace('\n', '') for l in f.readlines()]

class Node:
	def __init__(self, size, parent_name, children):
		self.size = size
		self.parent_name = parent_name
		self.children = children

tree = {'/': Node(0, None, set())}
curr_dirname = '/'
curr_dirpath = ['/']

for l in raw[1:]:
	args = l.split(' ')
	if args[0] == '$':
		if args[1] == 'cd':
			if args[2] == '..':
				curr_dirpath.pop()
			else:
				curr_dirpath.append(args[2])
			curr_dirname = '_'.join(curr_dirpath)
			if curr_dirname not in tree:
				parent_dirname = \
					'_'.join(curr_dirname.split('_')[:-1])
				tree[curr_dirname] = Node(0, parent_dirname, set()) 
		else:
			continue
	elif args[0] == 'dir':
		continue
	else:
		tree[curr_dirname].size += int(args[0])

for n in tree.values():
	try:
		tree[n.parent_name].children.add(n)
	except KeyError:
		continue

def accrue_children_size(node):
	for child in node.children:
		node.size += accrue_children_size(child)
	return node.size
accrue_children_size(tree['/'])

print(sorted([n.size for n in tree.values() if 70_000_000 - tree['/'].size + n.size >= 30_000_000])[0])
