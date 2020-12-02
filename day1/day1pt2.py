file = open('input', 'r')
lines = file.readlines()

target = 2020

for linea in lines:
	linea.strip()
	for lineb in lines:
		lineb.strip()
		for linec in lines:
			linec.strip()
			result = int(linea) + int(lineb) + int(linec)
			if result == target:
				print(linea, lineb, linec, target)
				finalres = int(linea) * int(lineb) * int(linec)
				print(finalres)
				exit()

file.close()