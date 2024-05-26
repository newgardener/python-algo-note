def largestPalindromic(num: str) -> str:
    frequency = {}
    for ch in num:
        if ch not in frequency:
            frequency[ch] = 1
        else:
            frequency[ch] += 1

    half = []
    numPairs = sorted([num for num in frequency if frequency[num] >= 2], reverse=True)
    for num in numPairs:
        if not half and num == "0":
            continue
        repeat = frequency[num] // 2
        half += [num] * repeat
        frequency[num] -= repeat * 2

    if half and "0" in frequency:
        repeat = frequency["0"] // 2
        half += ["0"] * repeat
        frequency["0"] -= repeat * 2

    middle = sorted([num for num in frequency if frequency[num] >= 1], reverse=True)

    if middle:
        result = half + [middle[0]] + half[::-1]
    else:
        result = half + half[::-1]

    return "".join(result)
