def is_antenna(c):
    if '0' <= c <= '9':
        return True
    if 'a' <= c <= 'z':
        return True
    if 'A' <= c <= 'Z':
        return True
    return False


def antinode(x):
    for i in range(1, len(x)):
        if 4 * i >= len(x):
            break
        print(i, 4 * i, x[i], x[4 * i])
        if len(x[i].intersection(x[4 * i])) >= 1:
            return True
    return False


f = open('test.txt', 'r')
lines = f.readlines()

n = len(lines)
m = len(lines[0].strip())
cnt = 0

for i in range(1):
    for j in range(7, 8):
        # print('****')
        antennas = [set() for _ in range(m * m + n * n)]
        for a in range(n):
            for b in range(m):
                if is_antenna(lines[a][b]):
                    print(lines[a][b], (i - a) ** 2 + (b - j)**2)
                    antennas[(i - a) ** 2 + (b - j)**2].add(lines[a][b])
        print(antennas)
        if antinode(antennas):
            print(i, j)
            cnt += 1
print(cnt)