# Problem link: https://adventofcode.com/2022/day/6/input

# Today the problem's input consists of only one line, so we can just read it directly
with open("Day6/input6.txt", "r") as f:
    data : str = f.readline().strip()

def solution(target : int):
    # For part 1 we need to find the first substring of our input 
    # that has a length of 4 and consists of unique characters. Then
    # we return the index of the last character of that substring.
    #
    # For example, if out input is 'bvwbjplbgvbhsrlpgdmjqwftvncz',
    # the answer would be 5, because the first substring of length 4
    # that consits of unique characters is 'vwbj', and 'j' is the 5th
    # character in the input.
    #
    # If you haven't solved any similar problems before you might go
    # for a brute force solution, taking every substring of length 4
    # and checking if it consists of unique characters. However, you 
    # would soon understand that if the length of the substring was greater
    # than 4, the brute force solution would take ages to complete as its
    # time complexity is O(n^2).
    # (For part 2 this is exactly what is being examined, as the target length is 14)
    #
    # There is a better way to solve this problem, in O(n) time complexity.
    # We have a list of characters that we have seen so far. We name this
    # list 'history'. We iterate the input using a 'pointer' variable that
    # starts at 0.
    #
    # For each character in the input, we check if it is in the history list.
    # If it's not, we just append it to the end of history and increment the
    # pointer. If it is, instead of starting over from the last apperance of
    # that character, we can just remove all the characters before it from the
    # history list (as they are added in the order they appear in the input).
    # This works because we know that every other character in the history list
    # after the one we just encoutered twice, is unique. So we don't need to check
    # again. This process is repeated until the length of history is the one requested.
    #
    # Example: if our input is 'mjqjpqmgbljsph'
    # 1. history = [], pointer = 0
    # 2. history = ['m'], pointer = 1
    # 3. history = ['m', 'j'], pointer = 2
    # 4. history = ['m', 'j', 'q'], pointer = 3
    # 5. As we proceed to add the 4th character (j), we see that it is already in the list.
    #    so we remove all the characters before it from the list, and add it normally.
    #    history = ['q', 'j'], pointer = 4
    # 6. history = ['q', 'j', 'p'], pointer = 5
    # 7. Then again, we see that the next character (q) is already in the list, so we remove
    #    all the characters before it from the list, and add it normally.
    #    history = ['j', 'p', 'q'], pointer = 6
    # 8. history = ['j', 'p', 'q', 'm'], pointer = 7
    # Here the length of history is 4, so we return the pointer, which is 7.
    pointer : int = 0
    history : set[str] = []
    
    while pointer < len(data):
        # If the character already exists in the history list
        if data[pointer] in history:
            # Remove all the characters before it (and itself) from the list
            history = history[history.index(data[pointer]) + 1:]

        # Add the character to the history list
        history.append(data[pointer])
        # Increment the pointer
        pointer += 1
        
        # If the length of the history list is the one requested
        if len(history) == target:
            # Return the pointer
            return pointer



if __name__ == "__main__":
    print(solution(4))
    print(solution(14))