import bisect


def jobScheduling(startTime: list[int], endTime: list[int], profit: list[int]) -> int:
    jobs = sorted(zip(startTime, endTime, profit))
    startTimes = [job[0] for job in jobs]
    dp = {}

    def dfs(i):
        if i == len(jobs):
            return 0

        if i in dp:
            return dp[i]

        # not include
        res = dfs(i + 1)

        # include
        j = bisect.bisect_left(startTimes, jobs[i][1])
        dp[i] = max(res, jobs[i][2] + dfs(j))
        return dp[i]

    return dfs(0)
