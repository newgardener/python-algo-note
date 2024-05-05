# class TrieNode:
#     def __init__(self):
#         self.children = {}  # Using a dictionary to hold child nodes for each letter
#         self.isEnd = False  # Flag to mark the end of a word


class Solution:
    def findCharIndices(self, text, char):
        return [
            index for index, current_char in enumerate(text) if current_char == char
        ]

    def indexPairs(self, text, words):
        result = []
        for word in words:
            startIndices = self.findCharIndices(text, word[0])
            # no matched case
            if not startIndices:
                continue

            for start in startIndices:
                startIndex, charIndex = start, 0
                isMatched = True
                while startIndex < len(text) and charIndex < len(word):
                    if text[startIndex] != word[charIndex]:
                        isMatched = False
                        break
                    startIndex += 1
                    charIndex += 1
                if isMatched:
                    result.append((start, startIndex - 1))

        return sorted(result)


text = "programmingisfun"
words = ["pro", "is", "fun", "gram"]
print(Solution().indexPairs(text, words))
