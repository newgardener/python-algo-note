class Solution:
    # stack 기반으로 구현하지 않았을 때
    # def nextLargerElement(self, arr):
    #     res = [-1] * len(arr)
    #     arr_sorted = sorted(arr)

    #     for i, num in enumerate(arr):
    #         if num == arr_sorted[-1] or i == len(arr) - 1:
    #             continue

    #         pointer = i + 1
    #         while pointer < len(arr):
    #             if arr[pointer] > num:
    #                 res[i] = arr[pointer]
    #                 break
    #             pointer += 1

    #     return res

    def nextLargerElement(self, arr):
        res = [-1] * len(arr)
        stack = [arr[-1]]

        for i in range(len(arr) - 2, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1]
            stack.append(arr[i])

        return res
