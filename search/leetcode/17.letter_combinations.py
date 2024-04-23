"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""


def letterCombinations(digits: str) -> list[str]:
    letterMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def dfs(index, combined):
        if len(combined) == len(digits):
            result.append(combined)
            return

        for i, digit in enumerate(digits[index:]):
            for letter in letterMap[digit]:
                dfs(i + 1, combined + letter)

    result = []

    if not digits:
        return result

    dfs(0, "")

    return result


print(letterCombinations("23"))
