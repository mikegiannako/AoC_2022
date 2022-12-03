from datetime import date

'''
This file contains some helpful functions for the parsing of the input
It is not a module, but rather a file that is imported into the solution.
So in order for it to work, it has to be in the same directory as the solution 
'''

# We automatically get the day from the datetime module
day_today : int = int(date.today().strftime("%d").lstrip("0"))

# Function to read data tha represent a 1D array
def rdln(sep : str = '\n') -> list[str]:
    with open(f"Day{day_today}/input{day_today}.txt", 'r') as f:
        data = f.read()
    return [x for x in data.split(sep) if x != '']

# Function to read data that represent a 2D array / 'board'
def rdbrd(sep : str = ' ', linesep : str = '\n') -> list[list[str]]:
    with open(f"Day{day_today}/input{day_today}.txt", 'r') as f:
        data : str = f.read()
    return [x.split(sep) for x in data.split(linesep) if x != '']

# Function to read data that represent a 3D array
def rd3d(sep : str = ',', linesep : str = '\n', chunksep : str = '\n\n') -> list[list[list[str]]]:
    with open(f"Day{day_today}/input{day_today}.txt", 'r') as f:
        data : str = f.read()
    return [[y.split(sep) for y in x.split(linesep) if y != ''] for x in data.split(chunksep)]

# Function that converts the data of a list to the specified type
# default is integers. This function is called recursively in case
# the data is a list of lists (or a list of lists of lists...)
def totype(data : list, target_type : type = int) -> list:
    res : list = []
    for element in data:
        if type(element) == list:
            temp = totype(element, target_type)
            if temp != []: res.append(temp)
            continue

        # Due to often parsing with newlines, there are some empty
        # strings which produce errors when converted to numerical values
        if element == '': continue

        # Thta's why we append to new list rather than doing something
        # like: [int(x) for x in data]
        res.append(target_type(element))

    return res

