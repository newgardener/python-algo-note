from collections import deque


def checkPalindrome(s):
    # remove all non-alphanumeric characters & convert to lower case
    s = "".join(filter(str.isalnum, s)).lower()
    q = deque(s)

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True
