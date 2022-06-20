import yaml
import re


with open("test1.yml","r",encoding="utf8") as file:
   
    test = yaml.load(file)
    print(test)
    if True:
        sqldata = test['curr_ods10']['sql']
        sqlparam =test['curr_ods10']['params']
        print(sqlparam)
        for i in range(1, ):
            sqldata = re.sub('\$' + str(i), str(sqlparam[i-1]), sqldata)
        print(sqldata)




# import os

# cwd = os.getcwd()

# print(cwd)
