"""

Task 1 **Technical Skills**

Given an input string s, find the length of the first longest substring without repeating characters.

"""


def length_of_longest_substring(given_string: str) -> int:
    n = len(given_string)
    longest = 0
    visited = set()
    i = j = 0
    while i < n and j < n:
        if given_string[j] not in visited:
            visited.add(given_string[j])
            j += 1
            longest = max(longest, j - i)
        else:
            visited.remove(given_string[i])
            i += 1
    return longest
