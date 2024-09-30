def longestIdealString(s: str, k: int) -> int:
    dp = [0] * 26  # max character length ending with each character from a to z

    for ch in s:
        idx = ord(ch) - ord('a')
        max_len = 0
        for i in range(26):
            if abs(i - idx) <= k:
                max_len = max(max_len, dp[i])
        dp[idx] = max_len + 1 # plus ch

    return max(dp)


