import math
def combo(line):
    line = line.strip().split()
    x = line[-2][2:-1]
    y = line[-1][2:]
    return int(x), int(y)

def min_sol(a_x, a_y, b_x, b_y, x, y):
    min_cost = math.inf
    for i in range(x // a_x + 10):
        if (x - a_x * i) % b_x == 0 and (y - a_y * i) % b_y == 0 and (x - a_x * i) // b_x == (y - a_y * i) // b_y:
            min_cost = min(min_cost, 3 * i + (x - a_x * i) // b_x)
    if min_cost == math.inf:
        return 0
    return min_cost


def mminsol(d, a_d, b_d):
    min_cost = math.inf
    for i in range(d // a_d + 10):
        if (d - i * a_d) % b_d == 0:
            min_cost = min(min_cost, 3 * i + (d - a_d * i) // b_d)
    if min_cost == math.inf:
        return 0
    re


f = open('input.txt', 'r')
lines = f.read().splitlines()
n = len(lines)
cnt = 0
for i in range(0, n, 4):
    a = lines[i]
    b = lines[i+1]
    c = lines[i+2]
    a_x, a_y = combo(a)
    b_x, b_y = combo(b)
    x, y = combo(c)

    cnt += min_sol(a_x, a_y, b_x, b_y, 10000000000000 + x, 10000000000000 + y)

print(cnt)