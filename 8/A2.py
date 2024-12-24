import math

def is_antenna(c):
    if '0' <= c <= '9':
        return True
    if 'a' <= c <= 'z':
        return True
    if 'A' <= c <= 'Z':
        return True
    return False


def antinodes(a, b):
    global field, n, m
    y1, x1 = a
    y2, x2 = b

    field[y1][x1] = 1
    field[y2][x2] = 1

    dx = x2 - x1
    dy = y2 - y1
    dx //= math.gcd(dx, dy)
    dy //= math.gcd(dy, dx)

    px, py = x1 - dx, y1 - dy
    while m > px >= 0 and n > py >= 0:
        field[py][px] = 1
        px -= dx
        py -= dy

    px, py = x1 + dx, y1 + dy
    while m > px >= 0 and n > py >= 0:
        field[py][px] = 1
        px += dx
        py += dy


f = open('input.txt', 'r')
lines = f.readlines()

n = len(lines)
m = len(lines[0].strip())
antennas = dict()
cnt = 0
field = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if is_antenna(lines[i][j]):
            if antennas.get(lines[i][j]) is None:
                antennas[lines[i][j]] = []
            antennas[lines[i][j]].append((i, j))

for a in antennas.keys():
    x = antennas[a]
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            antinodes(x[i], x[j])
            # print(x[i], x[j])
            # for ii in range(len(field)):
            #     cnt += sum(field[ii])
            #     print(*field[ii])
            # assert False


print(antennas)
cnt = 0
for i in range(len(field)):
    cnt += sum(field[i])
    print(*field[i])
print(cnt)