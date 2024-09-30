from collections import defaultdict


def longestStrChain(words: list[str]) -> int:
    words.sort(key=len)
    wordLenMap = defaultdict(list)
    for word in words:
        wordLenMap[len(word)].append(word)

    def has_one_diff(w1, w2):
        diff = 0
        l1, l2 = 0, 0
        while l2 < len(w2):
            if l1 < len(w1):
                if w1[l1] == w2[l2]:
                    l1 += 1
                    l2 += 1
                else:
                    l2 += 1
                    diff += 1
            else:
                diff += 1
                l2 += 1
        return diff == 1

    def dfs(word, chain_len):
        word_len = len(word)
        if word_len + 1 not in wordLenMap:
            return chain_len

        longest = chain_len
        for next_word in wordLenMap[word_len + 1]:
            if has_one_diff(word, next_word):
                longest = max(longest, dfs(next_word, chain_len + 1))
        return longest

    longest = 0
    for word in words:
        longest = max(dfs(word, 1), longest)
    return longest
