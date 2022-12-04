from tools.parsing import *

# Problem link: https://adventofcode.com/2022/day/4

# The input is of the following format:
#
# 1-3, 5-7
# 2-4, 4-8
# 3-5, 7-9
#
# So the last (inner) split is on the '-', and the first (outer) split is on the ','
# Last split to change lines in on '\n', so we have a 3d array (list of pairs of pairs)
#
# Final result (after converting to int) should look like:
#
# [[[1, 3], [5, 7]], [[2, 4], [4, 8]], [[3, 5], [7, 9]]]
data : list[list[list[int]]] = totype(rd3d(sep = '-', linesep = ',', chunksep='\n'), int)

# As we know that the input is of pairs with could make it a dictionary with descriptive
# keys so the code is more readable. I wrote a list comprehension to do this. It is long
# and unreadable but it's an optional step and it's not necessary to understand the solution.
#
# The final result after the below list comprehension is:
#
# [{'first': {'left': 1, 'right': 3}, 'second': {'left': 5, 'right': 7}}, ...]
pairs : list[dict[dict[int]]] = [{ 'first' : { 'left' : elem[0][0], 'right' : elem[0][1] }, 'second' : { 'left' : elem[1][0], 'right' : elem[1][1] } } for elem in data]

# The way we know if one of the pairs is fully contained in the other is by looking
# at the pairs as lines. 
#
#  - If the leftmost point of the first line is to the left of
# the leftmost point of the second line and 
#  - the rightmost point of the first line is to the right of the rightmost point of 
# the second line
#
# Then the first line fully contains the second line. This is true for the 
# other way around as well.
#
# Example 1: 2 - 7 contains 3 - 5
#
# 1 2 3 4 5 6 7 8 9 
#   -----------      2 - 7
#     -----          3 - 5
#
# Example 2: 2 - 6 and 4 - 8 do not contain each other
#
# 1 2 3 4 5 6 7 8 9
#   ---------        2 - 6
#       ---------    4 - 8
#
# So what we can do is subtract the endpoints of the first line from the endpoints of
# the second line and calculate the product of the results. If the product is negative (or 0)
# it means that one of them contains the other because the endpoints of the first line
# are on different sides (or onto) of the second line.
#
# Based on Example 1, we get: 
#
#  Leftmost points -> 2 - 3 = -1   (leftmost point of 2 - 7 is to the left of the leftmost point of 3 - 5)
#  Rightmost points -> 7 - 5 = 2   (rightmost point of 2 - 7 is to the right of the rightmost point of 3 - 5)
#  Product -> -1 * 2 = -2          (product is negative, so 2 - 7 contains 3 - 5 or vice versa)
#
# Based on Example 2, we get:
#
#  Leftmost points -> 2 - 4 = -2   (leftmost point of 2 - 6 is to the left of the leftmost point of 4 - 8)
#  Rightmost points -> 6 - 8 = -2  (rightmost point of 2 - 6 is to the left of the rightmost point of 4 - 8)
#  Product -> -2 * -2 = 4          (product is positive, so 2 - 6 and 4 - 8 do not contain each other becase both
#                                   endpoints of 2 - 6 are on the same side of their corresponding endpoints in 4 - 8)
def contained(pair: dict[dict[int]]):
    left_diff  : int = pair['first']['left'] - pair['second']['left']
    right_diff : int = pair['first']['right'] - pair['second']['right']
    return left_diff * right_diff <= 0

def part1():
    count: int = 0

    # For each pair we want to check if either the first of second pair 
    # is fully contained in the other pair
    for pair in pairs:
        if contained(pair): count += 1

    return count

def part2():
    count : int = 0

    # For the second part, we want to find all the pairs that overlap even by a single point with each other
    # Following the same mindset as in function 'contained', we can check if one line is completely to the left
    # or right of the other line. 
    # What we need is the opposite of that, so we can either find the above and subtract if from the total number
    # of pairs or we can form the opposite condition. I chose the first option.
    for pair in pairs:
        # Again, following the same logic, to check if a line is completely to the left or right of the other line
        # we can check if the leftmost point of the first line is to the right of the rightmost point of the second line
        # or if the rightmost point of the first line is to the left of the leftmost point of the second line.
        if pair['first']['left'] > pair['second']['right'] or pair['first']['right'] < pair['second']['left']: count += 1
    
    return len(pairs) - count

if __name__ == "__main__":
    print(part1())
    print(part2())
