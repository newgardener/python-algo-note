str = "abcabcbb"


def longestSubstring(s):
    used = {}
    result = []
    longest_str = ""
    max_length = start = 0

    for index, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
            result.append(longest_str)
            longest_str = longest_str[longest_str.index(char) + 1 :]
        else:
            max_length = max(max_length, index - start + 1)

        used[char] = index  # 현재 문자의 위치 삽입
        longest_str += char
    result.append(longest_str)
    return max_length, result


max_length, result = longestSubstring(str)
print("max_length: {}".format(max_length))
print("result: {}".format(result))
