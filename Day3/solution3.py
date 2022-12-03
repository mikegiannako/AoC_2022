from tools.parsing import *
import string 

# This is a string containing all lowercase and uppercase letters in order
letters : str = string.ascii_lowercase + string.ascii_uppercase

rucksacks : list[str] = rdln()

def part1():
    count : int = 0

    # One line for compartments:
    # compartments = [[sack[:len(sack)//2], sack[len(sack)//2:]] for sack in rucksacks]

    compartments : list[list[str]] = []

    # We need for each line to split it into 2 equal parts to form the compartments
    for sack in rucksacks:
        # Using list indices, we can split the line into 2 equal parts
        # by using the length of the line divided by 2
        # We then append the 2 parts to the compartments list
        compartments.append([sack[:len(sack)//2], sack[len(sack)//2:]])

    # One line for calculating the sum:
    # return sum([letters.index((set(compartment[0]) & set(compartment[1])).pop()) + 1 for compartment in compartments])

    # Then we need to find the one character that is in both compartments and find the
    # index of that character in the letters string incremented by 1 (because we want the
    # index to start at 1 and not 0)
    for compartment in compartments:
        # In python, we can use the & operator to find the intersection of 2 sets
        # So the line below converts the 2 compartments into sets and finds the intersection
        # of the 2 sets. The result is a set containing the character that is in both compartments
        #
        # Finally, because we know we are only gonna have 1 character in the intersection, we can
        # use the pop() method to get the character from the set and assign it to the variable
        char : chr = (set(compartment[0]) & set(compartment[1])).pop()

        count +=  letters.index(char) + 1

    # The sum of all indexes is the result
    return count

def part2():
    # In part 2, we don't split the compartments into 2 equal parts, but rather split the whole
    # rucksacks into groups of 3. Then we need to find the index of the character that appears
    # in all 3 sacks and add it to the count
    count : int = 0

    # One line for groups:
    # groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

    groups : list[list[str]] = []
    for i in range(0, len(rucksacks), 3):
        # Once again, using list indices, we can split the list into groups of 3.
        # What the [i:i+3] epxression does is that it goes to the i-th element and
        # counts 3 elements from there. So if i = 0, it will take the first 3 elements
        # and if i = 3, it will take the 4th, 5th and 6th elements and so on
        #
        # So the result of the expression is a list containing 3 elements, making 'groups'
        # a 2D array (or to be exact, a list of lists of strings)
        groups.append(rucksacks[i:i+3])

    # One line for calculating the sum:
    # return sum([letters.index((set(group[0]) & set(group[1]) & set(group[2])).pop()) + 1 for group in groups])

    # Now we need to find the character that appears in all 3 groups. We will use the same
    # method as in part 1, but instead of using 2 compartments, we will use 3 groups
    for group in groups:
        # We convert the group into a set and find the intersection of the 3 sets
        char : chr = (set(group[0]) & set(group[1]) & set(group[2])).pop()

        count +=  letters.index(char) + 1

    return count

if __name__ == "__main__":
    print(part1())
    print(part2())
