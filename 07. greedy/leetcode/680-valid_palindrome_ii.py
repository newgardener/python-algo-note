def validPalindrome(s: str) -> bool:
    def isPalindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return False

    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return isPalindrome(i + 1, j) or isPalindrome(i, j - 1)
        i += 1
        j -= 1
    return False
