from collections import deque

def add_neighbours(i, j):
    global g, heads, tails

    if j != m - 1 and int(lines[i][j]) + 1 == int(lines[i][j + 1]):
        graph[i * m + j].append(i * m + j + 1)
    if j != 0 and int(lines[i][j]) + 1 == int(lines[i][j - 1]):
        graph[i * m + j].append(i * m + j - 1)
    if i != m - 1 and int(lines[i][j]) + 1 == int(lines[i + 1][j]):
        graph[i * m + j].append((i + 1) * m + j)
    if i != 0 and int(lines[i][j]) + 1 == int(lines[i - 1][j]):
        graph[i * m + j].append((i - 1) * m + j)

    if int(lines[i][j]) == 0:
        heads.append(i * m + j)
    elif int(lines[i][j]) == 9:
        tails.append(i * m + j)

def bfs(s):
    global graph
    q = deque()
    visited = [False for _ in range(n * m)]
    num_paths = [0 for _ in range(n * m)]
    visited[s] = True
    num_paths[s] = 1
    q.append(s)
    destinations = set()
    c = 0

    while q:
        w = q.popleft()
        for x in graph[w]:
            if not visited[x]:
                if lines[x // m][x % m] == '9':
                    destinations.add(x)
                visited[x] = True
                q.append(x)

    for d in destinations:
        c += paths(s, d)
    return c


def paths(s, d):
    visited = [False] * n * m
    path_c = [0]
    paths_until(s, d, visited, path_c)
    return path_c[0]


def paths_until(u, d, visited, path_c):
    visited[u] = True
    if u == d:
        path_c[0] += 1
    else:
        for w in graph[u]:
            if not visited[w]:
                paths_until(w, d, visited, path_c)
    visited[u] = False


f = open('input.txt', 'r')
lines = f.readlines()
n = len(lines)
m = len(lines[0].strip())

graph = [[] for j in range(m * n)]
heads = []
tails = []

for i in range(n):
    for j in range(m):
        add_neighbours(i, j)

cnt = 0
for i in range(len(heads)):
    cnt += bfs(heads[i])
print(cnt)

