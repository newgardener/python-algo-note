def removeDuplicateLetters(s):
    for char in sorted(s):
        suffix = s[s.index(char):]
        if set(s) == set(suffix):
            return char + removeDuplicateLetters(suffix.replace(char, ''))

    