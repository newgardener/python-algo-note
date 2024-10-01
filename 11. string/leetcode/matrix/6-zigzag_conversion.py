def convert(s: str, numRows: int) -> str:
    rows = [[] for _ in range(numRows)]
    curr_row = 0
    step = 1
    for ch in s:
        rows[curr_row].append(ch)

        if curr_row == 0:
            step = 1
        elif curr_row == numRows - 1:
            step = -1
        curr_row += step

    return ''.join(''.join(row) for row in rows)
