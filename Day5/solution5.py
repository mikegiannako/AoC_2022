from datetime import date
import re
import copy

# Problem link: https://adventofcode.com/2022/day/5/input

# We automatically get the day from the datetime module
day_today : int = int(date.today().strftime("%d").lstrip("0"))

# The input of this problem is just impossible to parse
# and it looks like this: (Example input)
#
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
#
# so I split it into two parts, the first part contains the information
# of the initial state of the stacks, the second part contains the commands
with open(f"Day{day_today}/input{day_today}.txt", 'r') as f:
    parts : str = f.read().split("\n\n")
    # First part
    data : list[str] = parts[0].split('\n')
    # second part
    moves : list[str] = parts[1].split('\n')

# The commands were easy to parse, we just need some regex knowledge to only
# extract the numbers from the commands
#
# we use the re.findall() function to get all the numbers in the string
#
# The result of the below comprehension applied on the example input is as follows:
# [['1', '2', '1'], ['3', '1', '3'], ['2', '2', '1'], ['1', '1', '2']]
commands : list[list[str]] = [re.findall(r'(\d+)', line) for line in moves]

# Then, to make it more readable, we convert these number to a dictionary with more descriptive key names.
# Notice that we subtract 1 from the destination and source because the commands' numbers start at 1 but
# the list indexes start at 0. Count doesn't need to be subtracted because it's the number of letters we want to move
#
# The result of the below comprehension applied on the example input is as follows:
# [{'src': 1, 'dest': 0, 'cnt': 1}, {'src': 0, 'dest': 2, 'cnt': 3}, {'src': 1, 'dest': 0, 'cnt': 2}, {'src': 0, 'dest': 1, 'cnt': 1}]
commands : list[dict[str]] = [{'src': int(command[1]) - 1, 'dest': int(command[2]) - 1, 'cnt': int(command[0])} for command in commands]

# The stacks on the other hand were a bit more difficult to parse
# first we make our list of "stacks"
# The number of stacks is equal to len(data[0]) // 4 + 1 (because of the spaces and '[]'), no need to understand this
# The height of the highest stack is equal to len(data) - 1 (because of the numbers below the staks)
nostacks : int = len(data[0]) // 4 + 1
maxlenstack : int = len(data) - 1

# We create a list of lists, where each list represents a stack
stacks : list[list[str]] = [[] for i in range(nostacks)]

# We parse through the data and add the letters to the stacks
for i in range(nostacks):
    for j in range(maxlenstack):

        # Here the 1 + i * 4 is because of the spaces and '[]' in the data
        x = data[j][1 + i * 4]
        
        # We only add the letter if it is not a space
        if x != ' ':
            stacks[i].append(x)

    # We then reverse the list because the data should be read from the bottom to the top
    stacks[i] = stacks[i][::-1]

def part1():
    # We make a copy of the stacks so we don't modify the original
    stacks1 = copy.deepcopy(stacks)

    # We then execute the commands
    for command in commands:
        # Here we use some list slicing to move the letter from one stack to another
        # to avoid using a for loop as it would be slower. The way list slicing works
        # goes like this: list[start:stop:step] so if we do list[0:3] we get the first 3 elements.
        #
        # when you don't fill in start or stop in a slice it defaults to the start or end of the list.
        # So if we do [:3] we get the first 3 elements and if we do [3:] we get all elements from the 4th element
        #
        # It also works with negative numbers, so [-3:] would get the last 3 elements.
        # [-3:] is the same as [len(list) - 3:len(list)]
        #
        # That's what we use here to get the last n elements of a list where n is the 
        # number of letters we want to move. 
        # 
        # Then we take the slice we just produced and pass it through another slice that reverses 
        # the order of the elements. To reverse a list we do [::-1] which is the same as [len(list):0:-1]
        #
        # We want to reverse the letters we move for Part1 because that's how the 'Crane' works
        stacks1[command['dest']] += stacks1[command['src']][-command['cnt']:][::-1]

        # Then using the same syntax we remove the letters from the source stack
        stacks1[command['src']] = stacks1[command['src']][:-command['cnt']]

    # Then what we do is get the first letter of each stack (which is the last letter of each list)
    # and join them together to get the final string / message
    return ''.join([stack[-1] for stack in stacks1])


def part2():
    # For part 2 we do the exact same thing but when we move the letters from one stack to
    # another we don't reverse the order they get added to the destination stack
    stacks2 = copy.deepcopy(stacks)
    for command in commands:
        stacks2[command['dest']] += stacks2[command['src']][-command['cnt']:]
        stacks2[command['src']] = stacks2[command['src']][:-command['cnt']]

    return ''.join([stack[-1] for stack in stacks2])


if __name__ == "__main__":
    print(part1())
    print(part2())