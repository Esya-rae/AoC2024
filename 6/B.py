import copy

def rotate(di, dj):
    if di == -1:
        return 0, 1
    if di == 1:
        return 0, -1
    if dj == 1:
        return 1, 0
    return -1, 0

def is_loop(Y, oi, oj):
    global si, sj
    Y[oi][oj] = -1
    dirs = [[[] for _ in range(m)] for _ in range(n)]
    i = si
    j = sj
    di, dj = -1, 0
    num = 0
    while 0 <= i < n and 0 <= j < m:
        if (di, dj) in dirs[i][j]:
            return True
        dirs[i][j].append((di, dj))
        if Y[i][j] == -1:
            i -= di
            j -= dj
            di, dj = rotate(di, dj)
            if (di, dj) in dirs[i][j]:
                return True
        i += di
        j += dj
        num += 1
    return False



f = open('input.txt', 'r')
lines = f.readlines()
n = len(lines)
m = len(lines[0].strip())
X = [[] for _ in range(n)]
si, sj = 0, 0

for i in range(n):
    for j in range(m):
        if lines[i][j] == '.':
            X[i].append(0)
        if lines[i][j] == '#':
            X[i].append(-1)
        if lines[i][j] == '^':
            X[i].append(2)
            si, sj = i, j

cnt = 0
for oi in range(n):
    for oj in range(m):
        Y = copy.deepcopy(X)
        print(oi, oj)
        if Y[oi][oj] == 0 and is_loop(Y, oi, oj):
            # print(oi, oj)
            cnt += 1
print(cnt)



