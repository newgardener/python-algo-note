from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # base
    if not strs:
        return []

    wordDict = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in wordDict:
            wordDict[key] = [word]
        else:
            wordDict[key].append(word)

    return list(wordDict.values())
