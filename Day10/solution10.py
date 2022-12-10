# Problem link: https://adventofcode.com/2022/day/10/input

# Each day the problem descriptions become longer so I will not quite copy them
# here. If you want to read the full problem description, please visit the link
# I have provided above.

# This time the input is of the following format:
#
# noop
# addx 4
# addx -2
# noop
# addx 7
#
# So we split each line into 2 and same them into a list
# Result: [['noop'], ['addx', '4'], ['addx', '-2'], ['noop'], ['addx', '7']]
with open('Day10/input10.txt', 'r') as f:
    text : list[list[str]] = [line.split(' ') for line in f.read().splitlines()]

# We then convert the list in to a list of dictionaries to make
# the code later more readable
#
# Result: [{'type': 'noop', 'value': 0}, {'type': 'addx', 'value': 4}, 
#          {'type': 'addx', 'value': -2}, {'type': 'noop', 'value': 0}, 
#          {'type': 'addx', 'value': 7}]
#
# (Note: The value is an 0 if the line is a noop because it was easier to code it this way,
#  it's never going to be accessed anyways)
data : list[dict[str, str | int]] = [{'type': line[0], 'value': int(0 if len(line) == 1 else line[1])} for line in text]

def part1() -> int:
    # For part 1 we need to keep track of the value of x and the current cycle
    # Then we just check if the cycle is one of the ones we need to check and
    # if it is we add the value of x * cycle to the total. X starts at 1
    x : int = 1
    cycle : int = 0
    total : int = 0
    # The cycles we need to check are 20, 60, 100, 140, 180, 220
    checks : set[int] = {20, 60, 100, 140, 180, 220}

    # This is a function that represents the clock (of the CPU) ticking
    # for each clock tick we FIRST increment the cycle and then check if
    # the cycle is one of the ones we need to check. If it is we add the
    # value of x * cycle to the total
    def clock_tick() -> None:
        # Telling the function not to make new variables and use the
        # ones we have defined outside of the function
        nonlocal cycle, total
        cycle += 1
        if cycle in checks:
            total += (x * cycle)

    # Something to be noted here is that the 'noop' command takes 1 cycle
    # to execute, but the 'addx' command takes 2 cycles to execute. For
    # addx the value that comes with it is added to x AFTER the 2 cycles

    # For each command
    for command in data:

        # Either the command is noop or addx there will be at least 1 cycle
        clock_tick()

        # Then we check if the command is noop, if it is we continue to the next
        # command
        if command['type'] == 'noop': continue
        
        # If it isn't, (which means it's addx,) the clock ticks once more
        clock_tick()

        # And then we add the value of the command to x
        x += int(command['value']) # here I used int() because of type-checking errors
    
    # Finally we return the total
    return total

def part2() -> str:
    # For part 2 the question is quite different. We need to print a screen
    # based on the value of x and the cycle count. The screen is 40 characters
    # wide and 6 characters tall. The screen is filled with '.' and '#'s. The
    # value of X represents the middle position of a 3 character wide block.
    # For each cycle we check if the cycle count % 40 is within 1 of the value
    # of X. In that case we print a '#' otherwise we print a '.'. For more info
    # check the problem's full description.
    x : int = 1
    cycle : int = 0
    screen : str = ''

    # Here with each clock tick we FIRST 'draw' on the screen and then
    # increment the cycle count. Then we check if the cycle count is a multiple
    # of 40 (which means we reached the end of the line) and if it is we add a
    # newline to the screen
    def clock_tick():
        nonlocal cycle, screen
        screen += '#' if abs(cycle % 40 - x) <= 1 else '.'
        cycle += 1
        if(cycle % 40 == 0): screen += '\n'

    for command in data:

        # Same as before, either the command is noop or addx there will be at least 1 cycle
        clock_tick()

        if command['type'] == 'noop': continue
            
        clock_tick()

        x += int(command['value']) # here I used int() because of type-checking errors
    
    return screen

if __name__ == "__main__":
    print(part1())
    print(part2())
