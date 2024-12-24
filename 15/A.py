f = open('input.txt', 'r')
lines = f.read().splitlines()
field = []
x, y = 0, 0
i2 = 0

for i in range(len(lines)):
    l = lines[i].strip()
    if len(l) == 0:
        i2 = i
        break
    field.append([])
    for j in range(len(l)):
        if l[j] == '#':
            field[i].append(2)
        elif l[j] == 'O':
            field[i].append(1)
        elif l[j] == '.':
            field[i].append(0)
        else:
            y = i
            x = j
            field[i].append(0)

moves = ''
for i in range(i2 + 1, len(lines)):
    moves += lines[i].strip()

print(moves)

n = len(field)
m = len(field[0])

field[y][x] = 3
for i in range(n):
    print(*field[i])
field[y][x] = 0


for k in moves:
    # print(x, y, k)
    if k == '>':
        ex = x + 1
        while ex < m and field[y][ex] == 1:
            ex += 1
        if ex < m and field[y][ex] == 0:
            field[y][ex], field[y][x + 1] = field[y][x + 1], field[y][ex]
            x = x + 1
    elif k == '<':
        ex = x - 1
        while ex >= 0 and field[y][ex] == 1:
            ex -= 1
        if ex >= 0 and field[y][ex] == 0:
            field[y][ex], field[y][x - 1] = field[y][x - 1], field[y][ex]
            x = x - 1
    elif k == '^':
        ey = y - 1
        while ey >= 0 and field[ey][x] == 1:
            ey -= 1
        if ey >= 0 and field[ey][x] == 0:
            field[ey][x], field[y - 1][x] = field[y - 1][x], field[ey][x]
            y -= 1
    elif k == 'v':
        ey = y + 1
        while ey < m and field[ey][x] == 1:
            ey += 1
        if ey < m and field[ey][x] == 0:
            field[ey][x], field[y + 1][x] = field[y + 1][x], field[ey][x]
            y += 1

    # field[y][x] = 3
    # for i in range(n):
    #     print(*field[i])
    # field[y][x] = 0
    #
    # print()

cnt = 0
for i in range(n):
    for j in range(m):
        if field[i][j] == 1:
            cnt += 100 * i + j

print(cnt)