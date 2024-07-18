from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # create generic states of each word using "*"
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
