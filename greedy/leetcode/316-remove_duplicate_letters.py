def removeDuplicateLetters(s: str) -> str:
    sortedStr = sorted(s)
    requiredStr = set(s)

    for ch in sorted(list(requiredStr)):
        idx = s.find(ch)
        result = ch
        added = set([ch])
        if requiredStr.issubset(set(s[idx:])):
            while idx < len(s):
                if s[idx] not in added:
                    added.add(s[idx])
                    result += s[idx]
                idx += 1
            return result
