def rotate(di, dj):
    if di == -1:
        return 0, 1
    if di == 1:
        return 0, -1
    if dj == 1:
        return 1, 0
    return -1, 0


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

i = si
j = sj
di, dj = -1, 0
cnt = 1
flag = False
# num = 0
while 0 <= i < n and 0 <= j < m:
    # print(X[i][j])
    if X[i][j] == 2 and flag and di == -1 and dj == 0:
        break
    if X[i][j] == -1:
        i -= di
        j -= dj
        di, dj = rotate(di, dj)
    elif X[i][j] == 0:
        cnt += 1
        X[i][j] = 1
    i += di
    j += dj
    # print(X)
    # num += 1
    # if num == 10:
    #     break

print(cnt)


