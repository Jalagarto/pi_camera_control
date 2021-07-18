from inspect import getmembers, isfunction
import utils

functions_list = getmembers(utils, isfunction)

for i in functions_list:
    print(i[0])
