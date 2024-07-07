from typing import List

"""
Time Complexity: O(2^l * l) where l is the length of input string s
ㄴ considering all possible palindromic substrings
"""


# %%
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(s):
            return s == s[::-1]

        def dfs(partitions, substr):
            if not substr:
                result.append(partitions[:])
                return
            for i, ch in enumerate(substr):
                # single character
                if i == 0:
                    partitions.append(ch)
                    dfs(partitions, substr[i + 1:])
                    partitions.pop()
                # palindrome substr
                else:
                    if isPalindrome(substr[:i + 1]):
                        partitions.append(substr[:i + 1])
                        dfs(partitions, substr[i + 1:])
                        partitions.pop()

        dfs([], s)
        return result
