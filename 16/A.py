import math
import heapq
from collections import deque


def dijkstra():
    global graph, x, y
    start = (y * m + x) * 4 + 3
    # print(start)
    size = m * n * 4
    # print(graph[start])

    pq = []
    heapq.heappush(pq, (0, start))

    dist = [float('inf')] * size
    dist[start] = 0

    while pq:
        d, u = heapq.heappop(pq)

        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist

def best_places():
    global graph, x, y, fx, fy, m, n, dist
    along_path = set()
    fv = fy * m + fx
    q = deque()
    opt = min([dist[fv * 4], dist[fv * 4 + 1], dist[fv * 4 + 2], dist[fv * 4 + 3]])
    for i in range(4):
        if dist[fv * 4 + i] == opt:
            q.append(fv * 4 + i)
            along_path.add(fv * 4 + i)

    # print(q)
    while q:
        u = q.popleft()
        d = dist[u]
        # print(graph[u], dist[u])
        for v, w in graph[u]:
            if dist[v] == dist[u] - w and v not in along_path:
                q.append(v)
                along_path.add(v)
        uu = u // 4
        i = uu // m
        j = uu % m
        if i < n - 1 and u % 4 == 0:
            v = ((i + 1) * m + j) * 4
        elif j < m - 1 and u % 4 == 1:
            v = (i * m + j + 1) * 4 + 1
        elif i > 0 and u % 4 == 2:
            v = ((i - 1) * m + j) * 4 + 2
        elif j > 0 and u % 4 == 3:
            v = (i * m + j - 1) * 4 + 3

        # print(u, v)
        if dist[v] != math.inf:
            # print(dist[v])
            if dist[v] == dist[u] - 1 and v not in along_path:
                q.append(v)
                along_path.add(v)


    places = set()
    # print(len(along_path))
    for p in along_path:
        places.add(p // 4)
    return len(places)






f = open('input.txt', 'r')
lines = f.read().splitlines()
n = len(lines)
m = len(lines[0].strip())

field = []
for i in range(n):
    line = lines[i].strip()
    field.append([])
    for j in range(len(line)):
        if line[j] == 'S':
            x = j
            y = i
            field[-1].append(0)
        elif line[j] == 'E':
            fx = j
            fy = i
            field[-1].append(0)
        elif line[j] == '.':
            field[-1].append(0)
        else:
            field[-1].append(1)

graph = [[] for i in range(m * n * 4)]
for i in range(n):
    for j in range(m):
        if field[i][j] == 0:
            v = i * m + j
            vn = v * 4
            vw = v * 4 + 1
            vs = v * 4 + 2
            ve = v * 4 + 3

            vv = [vn, vw, vs, ve]
            for i2 in range(4):
                for j2 in range(i2 + 1, 4):
                    graph[vv[i2]].append((vv[j2], 1000))
                    graph[vv[j2]].append((vv[i2], 1000))

            if i > 0 and field[i - 1][j] == 0:
                graph[vn].append((((i - 1) * m + j) * 4, 1))
            if i < n - 1 and field[i + 1][j] == 0:
                graph[vs].append((((i + 1) * m + j) * 4 + 2, 1))
            if j > 0 and field[i][j - 1] == 0:
                graph[vw].append(((i * m + j - 1) * 4 + 1, 1))
            if j < m - 1 and field[i][j + 1] == 0:
                graph[ve].append(((i * m + j + 1) * 4 + 3, 1))

# print(graph)
dist = dijkstra()
# print(dist)
fv = fy * m + fx
print(min([dist[fv * 4], dist[fv * 4 + 1], dist[fv * 4 + 2], dist[fv * 4 + 3]]))
places = best_places()
print(places)
