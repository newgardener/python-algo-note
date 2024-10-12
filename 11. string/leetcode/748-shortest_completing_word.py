from collections import defaultdict, Counter


def shortestCompletingWord(licensePlate: str, words: list[str]) -> str:
    counts = defaultdict(int)
    for ch in licensePlate:
        if ch.isalpha():
            counts[ch] += 1

    words.sort(key=len)
    for w in words:
        if all(ch in w and w.count(ch) >= counts[ch] for ch in counts.keys()):
            return w
