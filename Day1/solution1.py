from tools.parsing import *

# Problem link: https://adventofcode.com/2022/day/1

data : list[list[int]] = totype(rdbrd(sep = '\n', linesep = '\n\n'), int)

def part1():
    # map function applies the given function to each element of the list
    # and returns a map object which is iterable. We would normally have to
    # convert it to a list but we can use the sum function directly on it
    return sum(map(sum, data))

def part2(): 
    # One line solution:
    #    return sum(sorted(list(map(sum, data)), reverse = True)[:3])
    
    # Same as part 1 but we need the sum of the 3 largest numbers
    # so we sort the list in descending order and take the first 3 elements.
    # Note that this time we have to convert the map object to a list
    num_list : list[int] = list(map(sum, data))
    num_list.sort(reverse = True)
    return sum(num_list[:3])

def main():
    print(part1())
    print(part2())
