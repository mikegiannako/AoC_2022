from tools.parsing import *

# Problem link: https://adventofcode.com/2022/day/9/input

# The input is of the following form:
# D 5
# U 12
# L 6
# R 8
text : list[list[str]] = rdbrd()

# As we then know that each line is a pair of Direction and Steps
# we convert our input to a dictinary with the fields 'dir' and 'steps'
# The form of the dictionary is:
# [{'dir': 'D', 'steps': 5}, {'dir': 'U', 'steps': 12}, 
#  {'dir': 'L', 'steps': 6}, {'dir': 'R', 'steps': 8}]
data = [{'dir': line[0], 'steps' : int(line[1])} for line in text]

# We then create a dictionary that maps the directions to a tuple
# of the form (x, y ) where x and y are the steps in the x and y direction
directions = {'D': (0, -1), 'U': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

def part1():
    # We create a set to keep track of the points the tail has visited
    # The good thing with a set is that if we add a point that is already in the set
    # it will not be added again so we don't need to check if the point already
    # exists in the set each time we add a point
    visited = set()

    # We start the head and tail at (0, 0)
    head = (0, 0)
    tail = (0, 0)
    # We add the starting point to the set
    visited.add(tail)

    # Then for each line in the input we move the head to the given direction
    # and move the tail based on the head's relative position to the tail
    for direction in data:
        for _ in range(direction['steps']):
            # We add to each coordinate the corresponding value from the directions dictionary
            # So if the direction is 'D' we add (0, -1) to the coordinates and the below code
            # would look like this:
            # head = (head[0] + directions['D'][0], head[1] + directions['D'][1])
            #      = (head[0] + 0                 , head[1] + -1)  
            head = (head[0] + directions[direction['dir']][0], head[1] + directions[direction['dir']][1])

            # Then we check if the head is two steps away from the tail in the x or y direction
            # if it is we move the tail the same way as the head and snap it to the x or y coordinate
            # of the head accordingly. Some movement examples are shown below:
            #   
            #            after head  after tail              after head
            #   before     moves       moves         before    moves
            #   .....      .....       .....         .....     .....      no tail
            #   .TH..  ->  .T.H.  -->  ..TH.         ..H..  -> ...H. ->  movement
            #   .....      .....       .....         ..T..     ..T..      needed
            #
            #            after head  after tail   after tail
            #   before     moves       moves        snaps
            #   .....      .....       .....        .....
            #   ..H..  ->  ...H.  -->  ...H.    ->  ..TH.
            #   .T...      .T...       ..T..        ..... 
            #    
            if abs(head[0] - tail[0]) == 2:
                tail = (tail[0] + directions[direction['dir']][0], head[1])
            elif abs(head[1] - tail[1]) == 2:
                tail = (head[0], tail[1] + directions[direction['dir']][1])
            
            # We then add the tail to the set of visited points
            visited.add(tail)
    # We then return the length of the set which is the number of unique points the tail has visited
    return len(visited)

def part2():
    # For part two, each the same exact process but the tail consists of 9 points intead of 1
    visited = set()

    # So we create a list of 10 poitns, the first point is the head and the rest are the tail
    rope = [(0, 0) for _ in range(10)]

    # This time we only care about he last point int the rope
    visited.add(rope[-1])
    for direction in data:
        for _ in range(direction['steps']):
            # For the head the process is the same as in part 1
            rope[0] = (rope[0][0] + directions[direction['dir']][0], rope[0][1] + directions[direction['dir']][1])

            # But for the tail we need to move each point in the tail as if the previous point that we moved is it's head
            for i in range(1, len(rope)):
                # We get the difference between the current point and the previous point in each axis
                # Here we don't use abs() because we want to know if the difference is positive or negative
                xdiff = rope[i - 1][0] - rope[i][0]
                ydiff = rope[i - 1][1] - rope[i][1]

                # This time there is one more case to consider, if the difference is 2 in both axes,
                # something that wasn't possible  before. Now it is possible in the following scenario:
                # (Consider 'H' as the head and each number as the according tail point)
                #
                # ......    ....H.    ....H.    ....H.    ....H.    ....H.    ....H.    ....H.
                # ....H.    ......    ....1.    ....1.    ....1.    ....1.    ....1.    ....1.
                # ....1. -> ....1. -> ...... -> ....2. -> ...32. -> ..432. -> ..432. -> ..432.
                # .432..    .432..    .432..    .43...    .4....    ......    ......    .5....
                # 5.....    5.....    5.....    5.....    5.....    5.....    5.....    6.....
                #
                # So in the above example we see that at the last 2 steps, tail piece number 4 was
                # already diagonnally aligned with piece number 5. Then piece number 4 has to move
                # yet again diagonally to touch piece number 3 (which is piece number 4's head). So
                # this created a situation where the difference in both axes is 2 between point 4 and 5.
                # In that case we move point 5 diagonally, something that wasn't possible in part 1.
                if abs(xdiff) == 2 and abs(ydiff) == 2:
                    rope[i] = (rope[i][0] + xdiff//abs(xdiff), rope[i][1] + ydiff//abs(ydiff))
                elif abs(xdiff) == 2:
                    rope[i] = (rope[i][0] + xdiff//abs(xdiff), rope[i - 1][1])
                elif abs(ydiff) == 2:
                    rope[i] = (rope[i - 1][0], rope[i][1] + ydiff//abs(ydiff))

            visited.add(rope[-1])
    return len(visited)

if __name__ == "__main__":
    print(part1())
    print(part2())
