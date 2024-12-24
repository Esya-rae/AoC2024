import math
import heapq
from collections import deque


def dijkstra():
    global graph, fx, fy, n, m
    start = fy * m + fx
    size = n * m

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


f = open('input.txt', 'r')
lines = f.read().splitlines()

n = len(lines)
m = len(lines[0].strip())
print(m, n)

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

graph = [[] for i in range(n * m)]
for i in range(n):
    for j in range(m):
        if field[i][j] == 0:
            v = i * m + j
            if i > 0 and field[i - 1][j] == 0:
                graph[v].append(((i - 1) * m + j, 1))
            if i < n - 1 and field[i + 1][j] == 0:
                graph[v].append(((i + 1) * m + j, 1))
            if j > 0 and field[i][j - 1] == 0:
                graph[v].append((i * m + j - 1, 1))
            if j < m - 1 and field[i][j + 1] == 0:
                graph[v].append((i * m + j + 1, 1))
d = dijkstra()
# print(d)

cheats = set()
ch = dict()
for i in range(n):
    for j in range(m):
        if field[i][j] == 0:
            v = i * m + j
            if i > 1 and field[i - 2][j] == 0 and field[i - 1][j] == 1:
                # dif = d[v] - d[(i - 2) * m + j] + 2
                # print(1, i, j, d[v] - d[(i - 2) * m + j])
                if d[v] - d[(i - 2) * m + j] >= 102:
                    cheats.add((v, (i - 2) * m + j))
            if i < n - 2 and field[i + 2][j] == 0 and field[i + 1][j] == 1:
                # print(2, i, j, d[v] - d[(i + 2) * m + j])
                if d[v] - d[(i + 2) * m + j] >= 102:
                    cheats.add((v, (i + 2) * m + j))
            if j > 1 and field[i][j - 2] == 0 and field[i][j - 1] == 1:
                # print(3, i, j, d[v] - d[i * m + j - 2])
                if d[v] - d[i * m + j - 2] >= 102:
                    cheats.add((v, i * m + j - 2))
            if j < m - 2 and field[i][j + 2] == 0 and field[i][j + 1] == 1:
                # print(4, i, j, d[v] - d[i * m + j + 2])
                if d[v] - d[i * m + j + 2] >= 102:
                    cheats.add((v, i * m + j + 2))

print(len(cheats))