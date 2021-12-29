def encryption(sentence, keyword, skips):
    front = []
    inserted = [[] for _ in range(len(sentence))]
    pos = -1

    while pos < len(sentence):
        for idx, skip in enumerate(skips):
            char = keyword[idx % len(keyword)]
            if skip == 0:
                if pos == -1:
                    front.append(char)
                else:
                    inserted[pos].append(char)
            else:
                if pos + skip >= len(sentence):
                    break
                for _ in range(skip):
                    pos += 1
                    if sentence[pos] == char:
                        break
                inserted[pos].append(char)
        break

    answer = ''
    answer += ''.join(front)
    for i in range(len(sentence)):
        answer += ''.join(sentence[i])
        if len(inserted[i]):
            answer += ''.join(inserted[i])
    
    return answer

print(encryption('abcde fghi', 'axyz', [3, 9, 0, 1]))
print(encryption('i love coding', 'mask', [0, 0, 3, 2, 3, 4]))
        