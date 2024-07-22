import collections
from collections import defaultdict
from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {ch: 0 for word in words for ch in word}

        # compare adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # there is no index i such that a[i] != b[i] and len(a) < len(b)
            # if w2 is prefix of w1, this is not lexicographically sorted
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            result = self.compareWords(w1[:minLen], w2[:minLen])
            # construct graph
            if result:
                # ch1 -> ch2
                ch1, ch2 = result
                # should check in order to increment indegree only once
                if ch2 not in graph[ch1]:
                    graph[ch1].add(ch2)
                    indegree[ch2] += 1

        # topological sort
        q = collections.deque([node for node in graph if graph[node] == 0])
        order = []
        while q:
            ch = q.popleft()
            order.append(ch)
            for neighbor in graph[ch]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return "".join(order) if len(order) == len(indegree) else ""

    def compareWords(self, word1, word2):
        for ch1, ch2 in zip(word1, word2):
            if ch1 != ch2:
                return [ch1, ch2]
        return None
