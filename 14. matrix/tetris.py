# given field(game board), figure(tetris), determine if one or more rows can be filled after figure is placed
def solution(field, figure):
    height = len(field)
    width = len(field[0])
    size = len(figure)

    for column in range(width - size + 1):
        # increment row if it's valid to reach to the bottom row
        row = 1
        while row < height - size + 1:
            can_fit = True
            for dx in range(size):
                for dy in range(size):
                    if field[row + dx][column + dy] == 1 and figure[dx][dy] == 1:
                        can_fit = False
            if not can_fit:
                break
            row += 1
        # revert back to prev row
        row -= 1

        for dx in range(size):
            is_row_filled = True
            for start in range(width):
                if not (
                    field[row + dx][start] == 1
                    or (
                        column <= start < column + size
                        and figure[dx][start - column] == 1
                    )
                ):
                    is_row_filled = False

            if is_row_filled:
                return column
        return -1
