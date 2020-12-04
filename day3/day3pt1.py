# get the forrest
file = open('input', 'r')
lines = file.read().split('\n')

# start position
x = 0 # horizontal
y = 0 # vertical

# x move value
xmove = 3

# trees
treecounter = 0
tree = "#"

#print("x\t y\t ground")

for line in lines:
	# dont move horizontally on first line
	if y > 0:
		# check if there is horizontal room to move
		if x <= len(line):
			x = (x + xmove) % len(line)
			#print(y, "\t", x, "\t", line[x])
			# check if char on current position is a tree
			if line[x] == tree:
				treecounter+=1
		else:
			print("Trees:", treecounter)
			break
	y+=1