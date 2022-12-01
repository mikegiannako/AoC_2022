from datetime import date

'''
This file contains some helpful functions for the parsing of the input
It is not a module, but rather a file that is imported into the solution.
So in order for it to work, it has to be in the same directory as the solution 
'''

# We automatically get the day from the datetime module
day_today : int = int(date.today().strftime("%d").lstrip("0"))

# Function to read the data from a file separated by the specified separator
def rdfile(sep : str = '\n') -> list[str]:
    with open(f"Day{day_today}/input{day_today}.txt", 'r') as f:
        data = f.read()
    return [x for x in data.split(sep)]

# Function that converts the data of a list to the specified type
# default is integers. This function is called recursively in case
# the data is a list of lists (or a list of lists of lists...)
def totype(data : list, target_type : type = int) -> list:
    res : list = []
    for element in data:
        if(type(element) == list):
            res.append(totype(element, target_type))
            continue

        # Due to often parsing with newlines, there are some empty
        # strings which produce errors when converted to numerical values
        if(element == ''): continue

        # Thta's why we append to new list rather than doing something
        # like: [int(x) for x in data]
        res.append(target_type(element))

    return res

def rdbrd(sep : str = ' ', linesep : str = '\n') -> list[list[str]]:
    with open(f"Day{day_today}/input{day_today}.txt", 'r') as f:
        data : str = f.read()
    return [x.split(sep) for x in data.split(linesep)]
