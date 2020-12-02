file = open('input', 'r')
lines = file.readlines()

target = 2020

for linea in lines:
	linea.strip()
	for lineb in lines:
		lineb.strip()
		result = int(linea) + int(lineb)
		if result == target:
			print(linea, lineb, target)
			finalres = int(linea) * int(lineb)
			print(finalres)

file.close()