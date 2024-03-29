# %% 최대 슬라이딩 윈도우
from collections import deque

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3


def maxSlidingWindow(nums, k):
    results = []
    window = deque()
    current_max = float("-inf")

    for i, v in enumerate(nums):
        window.append(v)
        if i < k - 1:
            continue

        # 새로 추가된 값이 기존 큰 값보다 큰 경우 교체
        if current_max == float("-inf"):
            current_max = max(window)
        elif v > current_max:
            current_max = v

        # current_max를 result 배열에 추가
        results.append(current_max)

        # 최대값이 window엣 빠질 경우 current_max 값 초기화
        if current_max == window.popleft():
            current_max = float("-inf")

    return results


print(maxSlidingWindow(nums, k))

# %% 부분 문자열이 포함된 최소 윈도우

from collections import Counter

S = "ADOBECODEBANC"
T = "ABC"


def minWindow(S, T):
    need = Counter(T)
    missing = len(T)

    left = start = end = 0
    for right, char in enumerate(S, 1):
        missing -= need[char] > 0
        need[char] -= 1

        if missing == 0:
            while left <= right and need[S[left]] < 0:
                need[S[left]] += 1
                left += 1

            if not end or right - left <= end - start:
                start, end = left, right

            need[S[left]] += 1
            missing += 1
            left += 1
    return S[start:end]


print(minWindow(S, T))

# %% 가장 긴 반복 문자 대체
from collections import Counter

s = "AAABC"
k = 2


def characterReplacement(s, k):
    left = 0
    counts = Counter()

    for right in range(1, len(s) + 1):
        counts[s[right - 1]] += 1
        # 가장 많이 등장하는 문자 개수
        max_char_n = counts.most_common(1)[0][1]
        # k 초과시 왼쪽 포인터 이동
        if right - left - max_char_n > k:
            counts[s[left]] -= 1
            left += 1

    return right - left


print(characterReplacement(s, k))
# %%
