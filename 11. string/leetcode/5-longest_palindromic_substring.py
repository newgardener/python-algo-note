def longestPalindrome(s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    result = ""
    for i in range(len(s)):
        result = max(result, expand(i, i), expand(i, i + 1), key=len)
    return result
