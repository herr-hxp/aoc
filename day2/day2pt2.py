file = open('day2input', 'r')
lines = file.readlines()

count = 0

for line in lines:
	# splitting the line
	line = line.split(":")

	# the policy
	policy = line[0].split(" ")
	
	# the password
	pw = line[1].split(" ")
	pw = pw[1]
	
	# the character
	char = policy[1]
	
	# the amount allowed of character x
	indexpolicy = policy[0].split("-")
	index1 = indexpolicy[0]
	index2 = indexpolicy[1]
	
	# check if char is present at index index1 xor index index2
	index1 = int(index1)
	index2 = int(index2)
	# policy doesn't account for index 0
	index1-=1
	index2-=1
	if (pw[index1] == char and not pw[index2] == char) or (not pw[index1] == char and pw[index2] == char):
		count+=1

print("Amount of valid passwords: ", count)