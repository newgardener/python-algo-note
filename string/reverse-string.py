from functools import reduce

"""
stack-based solution is also possible
"""


class Solution:
    def reverseString(self, s):
        return reduce(lambda a, b: a + b, s[::-1], "")

    # def reverseString(self, s):
    #     stack = list(s)
    #     reversed_str = ""

    #     while stack:
    #         reversed_str += stack.pop()

    #     return reversed_str
