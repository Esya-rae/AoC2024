from collections import deque


def find_neighbours(s):
    global m, n
    i = s // m
    j = s % m

    neighbours = []
    if i > 0:
        neighbours.append((i - 1) * m + j)
    if j > 0:
        neighbours.append(i * m + j - 1)
    if i < n - 1:
        neighbours.append((i + 1) * m + j)
    if j < m - 1:
        neighbours.append(i * m + j + 1)
    return neighbours


def calc_sides(shape):
    global n, m
    s = 0
    #vertical
    for j in range(m):
        #left
        i = 0
        while i < n:
            flag = 0
            while i < n and shape[i][j] and (j == 0 or not shape[i][j - 1]):
                flag = 1
                i += 1
            i += 1
            s += flag
        # right
        i = 0
        while i < n:
            flag = 0
            while i < n and shape[i][j] and (j == m - 1 or not shape[i][j + 1]):
                flag = 1
                i += 1
            i += 1
            s += flag
    # horizontal
    for i in range(n):
        # left
        j = 0
        while j < m:
            flag = 0
            while j < m and shape[i][j] and (i == 0 or not shape[i - 1][j]):
                flag = 1
                j += 1
            j += 1
            s += flag
        # right
        j = 0
        while j < m:
            flag = 0
            while j < m and shape[i][j] and (i == n - 1 or not shape[i + 1][j]):
                flag = 1
                j += 1
            j += 1
            s += flag
    return s



def bfs(s):
    global global_visited
    q = deque()
    visited = [False for _ in range(n * m)]
    shape = [[0 for _ in range(m)] for _ in range(n)]
    shape[s // m][s % m] = 1
    area = 1
    visited[s] = True
    global_visited[s] = True
    q.append(s)
    letter = letters[s]
    c = 0
    while q:
        w = q.popleft()
        wn = find_neighbours(w)
        for x in wn:
            if not visited[x]:
                if lines[x // m][x % m] == letter:
                    global_visited[x] = True
                    visited[x] = True
                    area += 1
                    q.append(x)
                    shape[x // m][x % m] = 1
    sides = calc_sides(shape)
    print(letter, area, sides)
    return area * sides


f = open('input.txt', 'r')
lines = f.read().splitlines()
n = len(lines)
m = len(lines[0].strip())
letters = [lines[k // m][k % m] for k in range(n * m)]
global_visited = [False for _ in range(n * m)]
cnt = 0


for i in range(n):
    for j in range(m):
        if not global_visited[i * m + j]:
            cnt += bfs(i * m + j)


print(cnt)

