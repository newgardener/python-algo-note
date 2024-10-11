def addStrings(num1: str, num2: str) -> str:
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    res = ""

    while i >= 0 and j >= 0 or carry == 1:
        if i >= 0:
            carry += ord(num1[i]) - ord("0")
            i -= 1
        if j >= 0:
            carry += ord(num2[j]) - ord("0")
            j -= 1

        res += chr((carry % 10) + ord("0"))
        carry //= 10

    return res[::-1]
