def combo(line):
    line = line.strip().split()
    p = line[0][2:].split(',')
    v = line[1][2:].split(',')
    x, y = int(p[0]), int(p[1])
    vx, vy = int(v[0]), int(v[1])
    return x, y, vx, vy

def is_tree():
    global field, n, m
    for i in range(n):
        for j in range(m):
            if field[i][j] > 1:
                return False

    return True



f = open('input.txt', 'r')
lines = f.read().splitlines()

n = 103
m = 101

for s in range(10000):
    field = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(len(lines)):
        x, y, vx, vy = combo(lines[i])
        fx = (x + vx * s) % m
        fy = (y + vy * s) % n
        field[fy][fx] += 1
    if is_tree():
        print(s)
        for i in range(n):
            print(*field[i])
