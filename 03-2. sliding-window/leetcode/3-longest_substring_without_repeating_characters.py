"""
n = length of string s, m = the number of unique character in string s
Time Complexity: O(n)
Space Complexity: O(m)
"""

# %%
# solution using set


def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l = 0
    longest = 0
    for r in range(len(s)):
        ch = s[r]
        # ensure not to add duplicate character into charSet
        while ch in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(ch)
        # calculate the length of longest, non-duplicate string every time
        longest = max(longest, r - l + 1)
    return longest


# %%
# solution using hashmap


def lengthOfLongestSubstring(s: str) -> int:
    # record index of each character
    charMap = {}
    l = 0
    longest = 0
    for r in range(len(s)):
        ch = s[r]
        # in order to retrieve duplicating character index right away: O(1)
        if ch in charMap:
            l = max(l, charMap[ch] + 1)
        charMap[ch] = r
        # calculate the length of longest, non-duplicate string every time
        longest = max(longest, r - l + 1)
    return longest
