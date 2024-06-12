import bisect
from typing import List


def jobScheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    jobs = sorted(zip(startTime, endTime, profit))
    dp = {}

    def dfs(i):
        if i == len(jobs):
            return 0

        if i in dp:
            return dp[i]

        # not include
        res = dfs(i + 1)

        # include
        j = bisect.bisect(jobs, (jobs[i][1], -1, -1))
        dp[i] = max(res, jobs[i][2] + dfs(j))
        return dp[i]

    return dfs(0)
