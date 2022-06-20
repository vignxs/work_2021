dict = {'a': 1, 'b': 2, 'c': 3}
print(dict)
dict = {value:key for key, value in dict.items()}
print(dict)