from functools import reduce

"""
input /= 2
input //= 2
의 차이
"""


class Solution:
    def decimalToBinary(self, num):
        input = num
        stack = []

        while input:
            if input % 2 == input:
                stack.append(int(input))
                break

            stack.append(input % 2)
            input /= 2

        return reduce(lambda x, y: x + str(y), reversed(stack), "")

    # def decimalToBinary(self, num):
    #     stack = []

    #     while num:
    #         stack.append(num % 2)
    #         num //= 2

    #     return "".join(str(i) for i in reversed(stack))
