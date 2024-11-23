def lengthOfLongestSubstring(s: str) -> int:
    maxLength = 0
    window = set()
    l = 0
    for r, ch in enumerate(s):
        if ch not in window:
            window.add(ch)
        else:
            while s[l] != ch:
                window.remove(s[l])
                l += 1
            l += 1
        maxLength = max(maxLength, r - l + 1)
    return maxLength



