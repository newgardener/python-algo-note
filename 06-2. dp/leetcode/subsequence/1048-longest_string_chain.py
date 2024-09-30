from collections import defaultdict


def longestStrChain(words: list[str]) -> int:
    word_set = set(words)
    dp = defaultdict(int)

    words.sort(key=len)

    word_chain = 0
    for word in words:
        # initialize a chain of word to 1
        dp[word] = 1
        for i in range(len(word)):
            prev = word[:i] + word[i+1:]
            if prev in word_set:
                dp[word] = max(dp[word], dp[prev] + 1)
        # update word_chain to be the longest
        word_chain = max(word_chain, dp[word])

    return word_chain


