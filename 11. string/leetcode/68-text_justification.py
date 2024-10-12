def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    words = [(w, len(w)) for w in words]
    res = []
    line = []
    width = 0
    i = 0
    while i < len(words):
        w, w_len = words[i]
        if width < maxWidth - w_len - len(words):
            line.append(w)
            width += w_len
            i += 1
        else:
            wcnt = len(line)
            need = maxWidth - width
            if wcnt == 1:
                sentence = "".join(line) + " " * need
            else:
                space_btw_word = need // (wcnt - 1)
                extra_space = need % (wcnt - 1)
                sentence = ""
                for j in range(wcnt):
                    sentence += line[j]
                    if j < wcnt - 1:
                        sentence += " " * space_btw_word
                        if j < extra_space:
                            sentence += " "
            res.append(sentence)
            line = []
            width = 0

    if line:
        lastline = " ".join(line)
        spaces = maxWidth - len(lastline)
        res.append(lastline + " " * spaces)

    return res
