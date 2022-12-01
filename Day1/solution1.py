from tools.parsing import *

def parse_input():
    with(open("Day1/input1.txt", "r")) as f:
        # Parses the input into a 2D list of strings
        data : list[list[str]] = rdbrd(sep = '\n', linesep = '\n\n')

        # Converts the data to integers
        int_data : list[list[int]] = totype(data, int)

        return int_data

def part1():
    # One line solution
    # with(open("Day1/input1.txt","r")) as f:
    #     return max(map(sum, totype(rdbrd(sep = '\n', linesep = '\n\n'), int)))

    data = parse_input()

    # map function applies the given function to each element of the list
    # and returns a map object which is iterable. We would normally have to
    # convert it to a list but we can use the sum function directly on it
    return sum(map(sum, data))

def part2(): 
    # One line solution
    # with(open("Day1/input1.txt","r")) as f: 
    #    return sum(sorted(list(map(sum, totype(rdbrd(sep = '\n', linesep = '\n\n'), int))), reverse = True)[:3])
    
    data = parse_input()

    # Same as part 1 but we need the sum of the 3 largest numbers
    # so we sort the list in descending order and take the first 3 elements.
    # Note that this time we have to convert the map object to a list
    num_list : list[int] = list(map(sum, data))
    num_list.sort(reverse = True)
    return sum(num_list[:3])

if __name__ == "__main__":
    print(part1())
    print(part2())
