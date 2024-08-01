class Solution:
    def getSum(self, a: int, b: int) -> int:
        # to retrieve only 32-bit value part
        mask = 0xFFFFFFFF
        # repeat until we have carries
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return a & mask if b > 0 else a

