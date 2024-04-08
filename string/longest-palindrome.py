from collections import Counter


def longestPalindrome(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ""
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result


def longestPalindromeEasy(s):
    counter = Counter(s)

    length = 0
    oddNumberFound = False

    for value in counter.values():
        if value % 2 == 0:
            length += value
        else:
            length += value - 1
            oddNumberFound = True

    if oddNumberFound:
        length += 1

    return length
