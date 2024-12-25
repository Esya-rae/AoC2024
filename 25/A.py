def to_num(x):
    heights = [-1] * 5
    for i in range(7):
        for j in range(5):
            if x[i][j] == '#':
                heights[j] += 1
    return heights


def fits(key, lock):
    for i in range(5):
        if (key[i] + lock[i]) > 5:
            return False
    return True


f = open('input.txt', 'r')
lines = f.readlines()
locks = []
keys = []

for i in range(0, len(lines), 8):
    if lines[i].strip() == '#####':
        locks.append(to_num(lines[i:i+7]))
    else:
        keys.append(to_num(lines[i:i+7]))
print(locks)
print(keys)
res = 0
for k in keys:
    for l in locks:
        if fits(k, l):
            res += 1
print(res)