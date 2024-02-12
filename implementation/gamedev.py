n, m = map(int, input().split())  # n(row), m(column)
x, y, direction = map(int, input().split())

game_map = []
for _ in range(n):
    game_map.append(list(map(int, input().split())))


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
count = 1
turn_count = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if game_map[nx][ny] == 0:
        game_map[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_count = 0
        continue
    else:
        turn_count += 1

    if turn_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if game_map[nx][ny] == 0:
            x = nx
            y = ny
            turn_count = 0
        else:
            break

print(count)
