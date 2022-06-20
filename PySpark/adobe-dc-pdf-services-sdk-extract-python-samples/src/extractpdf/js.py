# Python program to read
# json file


import json

# Opening JSON file
f = open('/home/vignxs/out/structuredData.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data.keys():
	print(data[i].keys())

# Closing file
f.close()
