def permutation(s: str):
    if len(s) == 1:
        return [s]
    else:
        perms = []
        for i in range(len(s)):
            for perm in permutation(s[:i] + s[i + 1 :]):
                perms.append(s[i] + perm)
        return perms
