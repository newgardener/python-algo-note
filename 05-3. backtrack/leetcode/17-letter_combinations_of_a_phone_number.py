from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def dfs(i, path):
            if not digits:
                return
            if i >= len(digits):
                res.append(path)
                return
            for ch in digitMap[digits[i]]:
                dfs(i + 1, path + ch)

        dfs(0, "")
        return res
