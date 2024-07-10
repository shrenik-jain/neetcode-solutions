'''
Question

Given a string, that consists of the characters 'A' and 'B' only, in one move, delete either an "AB" or a "BB" 
substring and concatenate the remaining substrings. Find the minimum possible length of the remaining string 
after performing any number of moves.

Note: A substring is a contiguous subsequence of a string.

Example s = "BABBA"
Using 0-based indexing, the following moves are optimal.
• Delete the substring "AB" starting at index 1 then, "BABBA" -> "BBA"
• Delete the substring "BB" starting at index 0 then, "BBA" -> "A"

There are no more moves, so the minimum possible length of the remaining string is 1.
'''

def min_length(s: str) -> int:
    """
    Returns the minimum possible length of the string s after applying the operations.
    """

    # create a stack to keep track of the last pushed character
    stack = []

    # iterate over all chars in string `s`
    for char in s:
        # if stack has chars and last character is 'A' or 'B' and current character is 'B' (making an 'AB' or 'BB')
        if stack and (
            (stack[-1] == 'A' and char == 'B') or
            (stack[-1] == 'B' and char == 'B') ):
            # remove the last character
            stack.pop()

        # else push the character
        else:
            stack.push(char)

    # return the remaining length of the stack
    return len(stack)

# Example usage
s = "ABBABB"
print(min_length(s))