from collections import deque
from copy import deepcopy


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
            field[i].append(2)
        elif l[j] == 'O':
            field[i].append(1)
            field[i].append(3)
        elif l[j] == '.':
            field[i].append(0)
            field[i].append(0)
        else:
            y = i
            x = j * 2
            field[i].append(0)
            field[i].append(0)

moves = ''
for i in range(i2 + 1, len(lines)):
    moves += lines[i].strip()

print(moves)

n = len(field)
m = len(field[0])

# field[y][x] = 5
# for i in range(n):
#     print(*field[i])
# field[y][x] = 0
# print()


for k in moves:
    # print(x, y, k)
    if k == '>':
        ex = x + 1
        while ex < m and (field[y][ex] == 1 or field[y][ex] == 3):
            ex += 1
        if ex < m and field[y][ex] == 0:
            ex = x + 1
            while ex < m and (field[y][ex] == 1 or field[y][ex] == 3):
                if field[y][ex] == 1:
                    field[y][ex] = 3
                else:
                    field[y][ex] = 1
                ex += 1
            field[y][ex] = 3
            field[y][x + 1] = 0
            x += 1
    elif k == '<':
        ex = x - 1
        while ex >= 0 and (field[y][ex] == 1 or field[y][ex] == 3):
            ex -= 1
        if ex >= 0 and field[y][ex] == 0:
            ex = x - 1
            while ex >= 0 and (field[y][ex] == 1 or field[y][ex] == 3):
                if field[y][ex] == 1:
                    field[y][ex] = 3
                else:
                    field[y][ex] = 1
                ex -= 1
            field[y][ex] = 1
            field[y][x - 1] = 0
            x -= 1
    elif k == '^':
        d = deque()
        s = set()
        d.append((x, y))
        s.add((x, y))
        stop = False
        while d:
            x1, y1 = d.popleft()
            if (x1, y1 - 1) not in s:
                if field[y1 - 1][x1] == 2:
                    stop = True
                    break
                if field[y1 - 1][x1] == 1:
                    s.add((x1, y1 - 1))
                    d.append((x1, y1 - 1))
                    s.add((x1 + 1, y1 - 1))
                    d.append((x1 + 1, y1 - 1))
                elif field[y1 - 1][x1] == 3:
                    s.add((x1, y1 - 1))
                    d.append((x1, y1 - 1))
                    s.add((x1 - 1, y1 - 1))
                    d.append((x1 - 1, y1 - 1))
        if stop:
            continue
        field2 = deepcopy(field)
        for x1, y1 in s:
            # print(x1, y1)
            if (x1, y1 + 1) not in s:
                field[y1][x1] = 0
            field[y1 - 1][x1] = field2[y1][x1]
        y -= 1

    elif k == 'v':
        d = deque()
        s = set()
        d.append((x, y))
        s.add((x, y))
        stop = False
        while d:
            x1, y1 = d.popleft()
            if (x1, y1 + 1) not in s:
                if field[y1 + 1][x1] == 2:
                    stop = True
                    break
                if field[y1 + 1][x1] == 1:
                    s.add((x1, y1 + 1))
                    d.append((x1, y1 + 1))
                    s.add((x1 + 1, y1 + 1))
                    d.append((x1 + 1, y1 + 1))
                elif field[y1 + 1][x1] == 3:
                    s.add((x1, y1 + 1))
                    d.append((x1, y1 + 1))
                    s.add((x1 - 1, y1 + 1))
                    d.append((x1 - 1, y1 + 1))
        if stop:
            continue
        field2 = deepcopy(field)
        for x1, y1 in s:
            # print(x1, y1)
            if (x1, y1 - 1) not in s:
                field[y1][x1] = 0
            field[y1 + 1][x1] = field2[y1][x1]
        y += 1

    # field[y][x] = 5
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