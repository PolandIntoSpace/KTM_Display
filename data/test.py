import json

file = open("green.txt", "r")
filestr = file.read()
print(filestr)
file.close()

print('next try\n')

with open("green.json") as json_data:
	d = json.load(json_data)
	print(d)
	print(d.get('phase'))
	print(d.get('seconds'))

