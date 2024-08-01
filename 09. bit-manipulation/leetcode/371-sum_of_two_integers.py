"""
Why we should use mask?
- in order to represent 32-bit integer representation
ㄴ Python uses arbitrary-precision integers, which can grow to use as much memory as necessary to represent the integer
ㄴ 32-bit mask helps us simulate 32-bit integer
"""

"""
Take-Away:
- XOR (a ^ b): sum without carry
- AND + LEFT SHIFT (a & b) << 1: calculate the carry
- repeat until there is no more carries
"""


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
