from tools.parsing import *

# Saving the position of each option in a dictionary so we
# don't have to find it via "index" called on a list every time
index : dict = {'X': 0, 'Y': 1, 'Z': 2, 'A' : 0, 'B' : 1, 'C' : 2}

# For each of our answers we pair the according score
value : dict = {'X': 1, 'Y': 2, 'Z': 3}

# Loading the data, converting to string even if it's already a string
# So the 'totype' function eliminates empty strings/lists
data : list[list[chr]] = totype(rdbrd(sep = ' ', linesep = '\n'), str)

def part1() -> int:
    # This function calculates the score of a "game" of RPS
    # based on the index of each answer
    def calc_score(elf : chr, player : chr) -> int:

        # These are all the possible combinations of the 
        # subtraction between two indexes
        #
        # Rock  Paper Scissors
        # A(0), B(1), C(2)
        # X(0), Y(1), Z(2)
        #
        # If the result is 0, it means we have a Draw (3 points)
        # If the result is 1 or -2, it means the player won (6 points)
        # If the result is -1 or 2, it means the elf won (0 points)
        points : dict = {-2 : 6, -1 : 0, 0 : 3, 1 : 6, 2 : 0}

        return points[index[player] - index[elf]]


    # One line: return sum([calc_score(game[0], game[1]) + value[game[1]] for game in data])

    # Final sum
    count : int = 0

    # For each game
    for game in data:
        count += calc_score(game[0], game[1])
        count += value[game[1]]

    return count

def part2() -> int:
    # This time, 'X' means we have to lose, 'Y' means we have to draw
    # and 'Z' means we have to win
    score : dict = {'X': 0, 'Y': 3, 'Z': 6}
    offset : dict = {'X': -1, 'Y': 0, 'Z': 1}
    to_symbol : dict = ['X', 'Y', 'Z']

    # If we again take a look at the two "arrays":
    #
    # Rock  Paper Scissors
    # A(0), B(1), C(2)
    # X(0), Y(1), Z(2)
    #
    # We can see that in order to win, we have to subtract 1 from the index,
    # in order to draw, we have to pick the one with the same index and
    # in order to lose, we have to add 1 to the index

    # This function calculates the score of a "game" of RPS
    # based on the index of each answer
    def calc_score(elf : chr, player : chr) -> int:

        # Here the calculation is a bit different and looks complex but is 
        # actually quite simple. 
        #
        # First have to find the index of the elf's answer which results in (0, 1, 2). 
        #
        # Then, we add the offset that we need to move in order to win, draw or lose accordingly.
        #
        # Then we take the modulo of the result with 3 so that we don't go out of bounds.
        # (In Python, the modulo operator works perfectly with negative numbers in such cases.
        # For example, -1 % 3 = 2 which is the wrap-around action we want for -1)
        #
        # Final We convert the result to a symbol ('X', 'Y', 'Z') and return the score that
        # corresponds to that symbol
        return value[to_symbol[(index[elf] + offset[player]) % 3]]


    # One line: return sum([calc_score(game[0], game[1]) + score[game[1]] for game in data])

    # Final sum
    count : int = 0

    # For each game
    for game in data:
        count += calc_score(game[0], game[1])
        count += score[game[1]]
    

    return count

if __name__ == "__main__":
    print(part1())
    print(part2())
