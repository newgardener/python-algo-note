from collections import defaultdict, Counter


def shortestCompletingWord(licensePlate: str, words: list[str]) -> str:
    counts = defaultdict(int)
    for ch in licensePlate:
        if ch.isalpha():
            counts[ch] += 1

    words.sort(key=len)
    for w in words:
        w_cnt = Counter(w)
        if all(ch in w_cnt and w_cnt[ch] >= counts[ch] for ch in counts.keys()):
            return w
