def combo(line):
    line = line.strip().split()
    p = line[0][2:].split(',')
    v = line[1][2:].split(',')
    x, y = int(p[0]), int(p[1])
    vx, vy = int(v[0]), int(v[1])
    return x, y, vx, vy


f = open('input.txt', 'r')
lines = f.read().splitlines()

cnt_00 = 0
cnt_01 = 0
cnt_10 = 0
cnt_11 = 0

n = 103
m = 101

# n = 7
# m = 11
#
# field = [[0 for _ in range(m)] for _ in range(n)]

for i in range(len(lines)):
    x, y, vx, vy = combo(lines[i])
    fx = (x + vx * 100) % m
    fy = (y + vy * 100) % n
    # field[fy][fx] += 1
    if fx < m // 2:
        if fy < n // 2:
            cnt_00 += 1
        elif fy > n // 2:
            cnt_01 += 1
    elif fx > m // 2:
        if fy < n // 2:
            cnt_10 += 1
        elif fy > n // 2:
            cnt_11 += 1
    # print(fx, fy)

#
# for i in range(n):
#     print(*field[i])

print(cnt_00, cnt_01, cnt_10, cnt_11)
print(cnt_00 * cnt_01 * cnt_10 * cnt_11)

