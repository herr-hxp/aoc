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
	amount = policy[0].split("-")
	charmin = amount[0]
	charmax = amount[1]
	
	#print("Password \"",pw,"\" should contain a minumum of", charmin, "and a maximum of", charmax, "of the character \"",char,"\"")

	# count the amount of char X in password
	charcount = pw.count(char)
	
	# check if charcount is gt charmin and ls charmax
	charmin = int(charmin)
	charmax = int(charmax)
	charcount = int(charcount)
	#print(charmin, charcount, charmax)
	while charmin <= charcount <= charmax:
		count+=1
		break

print("Amount of valid passwords: ", count)