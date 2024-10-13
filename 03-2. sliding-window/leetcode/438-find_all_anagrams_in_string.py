from collections import Counter

def findAnagrams(s: str, p: str) -> list[int]:
    w = len(p)
    window = Counter(s[:w])
    need = Counter(p)
    i = 0
    res = []
    while i < len(s):
        if i > 0:
            window[s[i+w-1]] += 1

        if all(need[ch] == window[ch] for ch in window):
            res.append(i)

        window[s[i]] -= 1
        i += 1
    return res