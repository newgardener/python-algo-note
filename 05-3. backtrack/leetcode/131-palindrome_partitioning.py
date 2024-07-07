from typing import List

"""
Time Complexity: O(2^l * l) where l is the length of input string s
ㄴ considering all possible palindromic substrings
"""

# %%
"""
Solution 1 - passing remaining substr to recursive function dfs
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def isPalindrome(s):
            return s == s[::-1]

        def dfs(substr):
            if not substr:
                result.append(part[:])
                return
            for i, ch in enumerate(substr):
                # single character
                if i == 0:
                    part.append(ch)
                    dfs(substr[i + 1:])
                    part.pop()
                # palindrome substr
                else:
                    if isPalindrome(substr[:i + 1]):
                        part.append(substr[:i + 1])
                        dfs(substr[i + 1:])
                        part.pop()

        dfs(s)
        return result


# %%
"""
Solution 2 - passing current string index to recursive function dfs
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def isPalindrome(s):
            return s == s[::-1]

        def dfs(i):
            if i >= len(s):
                result.append(part[:])
                return
            for j in range(i, len(s)):
                if isPalindrome(s[i:j + 1]):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return result
