from queue import Queue


class Solution:
    def generateBinaryNumbers(self, n):
        q = Queue()
        q.put("1")

        res = []
        while n > 0:
            res.append(q.get())
            s1 = res[-1] + "0"
            s2 = res[-1] + "1"
            q.put(s1)
            q.put(s2)
            n -= 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.generateBinaryNumbers(5))
