# https://leetcode.com/problems/largest-palindromic-number


def largestPalindromic(num: str) -> str:
    freq = [0] * 10  # count frequency of each digit from '0' to '9'
    for digit in num:
        freq[int(digit)] += 1

    firstHalf, middle = [], ""
    for i in range(9, -1, -1):
        # assign the largest odd count number to middle
        if freq[i] % 2 != 0 and middle == "":
            middle = str(i)
        firstHalf.extend([str(i)] * (freq[i] // 2))

    # case for only middle or nothing
    if not firstHalf:
        return middle if middle else "0"
    # case for all zeros
    elif all(d == "0" for d in firstHalf):
        return "0"
    return "".join(firstHalf) + middle + "".join(firstHalf[::-1])
