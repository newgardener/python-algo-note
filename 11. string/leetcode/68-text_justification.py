"""
Let N = number of words, L = average word length, M = maxWidth
Time Complexity: O(N * L)
- added to a sentence: O(1)
- formatted in process_sentence: O(L)
- total per word: O(L)
- all words: O(N * L)
at worst, L can be maxWidth, so O(N * M)

Space Complexity: O(N * M) for the output
"""

def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    def process_sentence(sentence):
        width = len(''.join(sentence))
        space_needed = maxWidth - width
        if len(sentence) == 1:
            return sentence[0] + ' ' * space_needed
        else:
            gap = len(sentence) - 1
            space, extra = divmod(space_needed, gap)
            formatted = ''
            for i, word in enumerate(sentence):
                formatted += word
                if i < len(sentence) - 1:
                    formatted += ' ' * (space + (1 if i < extra else 0))
            return formatted

    output = []
    sentence = []
    acc = 0
    for i, word in enumerate(words):
        space_needed = 1 if sentence else 0
        if acc + space_needed + len(word) <= maxWidth:
            acc += len(word)
            if len(sentence) > 0:
                acc += 1
            sentence.append(word)
        else:
            # process sentence first
            output.append(process_sentence(sentence))
            # and then add the next sentence word
            sentence = [word]
            acc = len(word)

    # process the last line to be left-justified
    last_line = ' '.join(sentence)
    last_line += ' ' * (maxWidth - len(last_line))
    output.append(last_line)
    return output

