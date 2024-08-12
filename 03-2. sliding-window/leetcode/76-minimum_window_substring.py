"""
Time Complexity: O(N)
ㄴ key point: compare one character at a time whether it meets the required condition
"""


def minWindow(s: str, t: str) -> str:
    # edge case
    if t == "" or len(s) < len(t):
        return ""

    countT, window = {}, {}
    for ch in t:
        countT[ch] = countT.get(ch, 0) + 1

    # use these variables to check whether window includes all characters in t
    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity")
    l = 0
    for r in range(len(s)):
        ch = s[r]
        window[ch] = window.get(ch, 0) + 1

        # check one character at a time => O(1)
        if ch in countT and window[ch] == countT[ch]:
            have += 1

        while have == need:
            # update the result
            size = r - l + 1
            if size < resLen:
                resLen = size
                res = [l, r]

            # move the left pointer by one
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1

    l, r = res
    return s[l: r + 1]
