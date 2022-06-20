# Python program to read
# json file

#
# import json
#
# # Opening JSON file
# f = open('names.json',)
#
# # returns JSON object as
# # a dictionary
# data = json.load(f)
#
# # Iterating through the json
# # list
# for i in data:
# 	print(i)
#
# # Closing file
# f.close()
import pandas
df = pd.read_json('names.json')



df