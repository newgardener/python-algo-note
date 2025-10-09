from collections import defaultdict, deque
from typing import List

"""
Time Complexity:
N = len(wordList), M = the length of each word
preprocessing (patternDict): O(N * M^2)
- given there are N words, each of length M word takes O(M) time to create pattern strings
BFS: O(N * M^2) at worst case
=> O(N * M^2)

Space Complexity: O(N * M^2)
- patternDict: O(N * M^2) in worst case, when all words are different and have no common patterns
- queue and seen set: O(N * M)
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # create generic states of each word using "*" (wild card)
        patternDict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patternDict[pattern].append(word)

        # (word, transformCnt)
        q = deque([(beginWord, 1)])
        seen = {beginWord}
        while q:
            word, count = q.popleft()
            # found endWord
            if word == endWord:
                return count
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                for transform in patternDict[pattern]:
                    if transform not in seen:
                        seen.add(transform)
                        q.append((transform, count + 1))
        # not found endWord
        return 0
