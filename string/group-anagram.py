from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for str in strs:
        anagrams[''.join(sorted(str))].append(str)
    return list(anagrams.values())

