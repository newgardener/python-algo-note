def removeDuplicateLetters(s: str) -> str:
    count = {char: s.count(char) for char in set(s)}
    result = []  # stack for the result string
    present = set()  # set to track if a character is in the result

    for char in s:
        if char not in present:
            while result and char < result[-1] and count[result[-1]] > 0:
                present.remove(result.pop())
            result.append(char)
            present.add(char)
        count[char] -= 1

    return "".join(result)
