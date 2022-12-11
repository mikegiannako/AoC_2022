import re
from tools.parsing import *
from copy import deepcopy

# Problem link: https://adventofcode.com/2022/day/11/input

# To see the input file go to the link above and click the "Get your puzzle input" button
with open("Day11/input11.txt", "r") as f:
    data : list[str] = f.read().split('\n\n')

# We make an array of dictionaries, each dictionary represents a monkey
monkeys : list[dict] = []
# We keep track of the greatest common divisor of all the check values
# because the numbers get really big really quickly
gcd : int = 1

# Parsing the input
for block in data:
    # We divide the input into lines
    lines = block.split('\n')

    monkey : dict = {}
    # We use regex to get the numbers from the input and convert them to integers
    monkey["items"] = totype(re.findall(r"(\d+)", lines[1]), int)
    # Here I save the whole operation string because I don't like
    # using many if statements. I just use eval() to evaluate the string (not recommended)
    monkey["operation"] = lines[2].split('=')[1].strip()
    # For the next 3 lines we just need to find the number of each line
    monkey["check"] = int(re.findall(r"(\d+)", lines[3])[0])
    monkey["true"] = int(re.findall(r"(\d+)", lines[4])[0])
    monkey["false"] = int(re.findall(r"(\d+)", lines[5])[0])
    monkey["count"] = 0

    # Calculating the greatest common divisor
    gcd *= monkey["check"]

    # We add the monkey to the list
    monkeys.append(monkey)

def part1():
    # We make a deep copy of the monkeys list so we don't modify the original
    lmonkeys = deepcopy(monkeys)

    divisor = 3

    # For each round we simulate the whole process described in the problem
    for _ in range(20):
        # For every monkey
        for monkey in lmonkeys:
            # For every item in the monkey's list
            while monkey["items"]:
                # Wee increment the amount of operations the monkey has done
                monkey["count"] += 1

                # We get the first item of the list (order doesn't really matter)
                item = monkey["items"].pop(0)

                # We evaluate the operation string replacing "old" with the item's value.
                # Again, eval is not generally recommended, especially with file input from the internet. However,
                # knowing that the input is safe, it's the most easy (and in my opinion, elegant) way to do it.
                temp = int(eval(monkey["operation"].replace("old", str(item))))

                # We divide the result by the divisor 
                temp = temp // divisor
                
                # Here it looks a bit confusing but this syntax prevents us from having to use indented blocks
                # What we do is the following:
                # Each monkey has a "true" and a "false" key. These keys represent the index of the monkey that
                # will receive the item if the result of the operation is divisible by the monkey's check value.
                # We use the modulo operator to check if the result is divisible by the check value.
                # So monkeys[monkey["true" if temp % monkey["check"] == 0 else "false"]] is the monkey that will
                # receive the item. 
                lmonkeys[monkey["true" if temp % monkey["check"] == 0 else "false"]]["items"].append(temp % gcd)

    # We sort the monkeys by the amount of operations they have done
    lmonkeys.sort(key=lambda x: x["count"], reverse=True)
    
    # We return the product of the first two monkeys
    return lmonkeys[0]["count"] * lmonkeys[1]["count"] 
    

def part2():
    # Exactly the same as part 1 but with 10_000 rounds
    # and no divisor
    lmonkeys = deepcopy(monkeys)

    for _ in range(10_000):
        for monkey in lmonkeys:
           while monkey["items"]:
                monkey["count"] += 1

                item = monkey["items"].pop()
                temp = int(eval(monkey["operation"].replace("old", str(item))))
                
                lmonkeys[monkey["true" if temp % monkey["check"] == 0 else "false"]]["items"].append(temp % gcd)

    lmonkeys.sort(key=lambda x: x["count"], reverse=True)
    return lmonkeys[0]["count"] * lmonkeys[1]["count"] 

if __name__ == "__main__":
    print(part1())
    print(part2())
