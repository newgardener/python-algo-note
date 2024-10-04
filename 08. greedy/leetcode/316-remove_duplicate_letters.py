"""
Time Complexity: O(N)
Space Complexity: O(N)
"""

# %%


"""
- set to keep track of occurrences of each character
- stack to record the order of characters
"""


def removeDuplicateLetters(s: str) -> str:
    count = {char: s.count(char) for char in set(s)}
    stack = []  # stack for the result string
    present = set()  # set to track if a character is in the result

    for char in s:
        if char not in present:
            while stack and char < stack[-1] and count[stack[-1]] > 0:
                present.remove(stack.pop())
            stack.append(char)
            present.add(char)
        count[char] -= 1

    return "".join(stack)


# %%

"""
- set to record the last occurrence of each character
"""


def removeDuplicateLetters(s: str) -> str:
    stack = []
    seen = set()

    last_occurrence = {c: i for i, c in enumerate(s)}

    for i, char in enumerate(s):
        if char not in seen:
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.discard(stack.pop())

            seen.add(char)
            stack.append(char)

    return "".join(stack)
