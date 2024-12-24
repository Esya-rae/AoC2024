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

def bfs(s):
    global global_visited
    q = deque()
    visited = [False for _ in range(n * m)]
    area = 1
    p = 0
    visited[s] = True
    global_visited[s] = True
    q.append(s)
    letter = letters[s]
    c = 0
    while q:
        w = q.popleft()
        wn = find_neighbours(w)
        p += 4 - len(wn)
        for x in wn:
            if not visited[x]:
                if lines[x // m][x % m] == letter:
                    global_visited[x] = True
                    visited[x] = True
                    area += 1
                    q.append(x)
                else:
                    p += 1
    return area * p


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

