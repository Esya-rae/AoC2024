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
        for i_2 in range(max(i - 20, 0), min(i + 21, m)):
            for j_2 in range(max(j - 20, 0), min(j + 21, n)):
                if field[i][j] == 0 and field[i_2][j_2] == 0:
                    if abs(i - i_2) + abs(j - j_2) <= 20:
                        # start = False
                        # finish = False
                        # if i_2 > i:
                        #     if field[i + 1][j] == 1:
                        #         start = True
                        #     if field[i_2 - 1][j] == 1:
                        #         finish = True
                        # if i_2 < i:
                        #     if field[i - 1][j] == 1:
                        #         start = True
                        #     if field[i_2 + 1][j] == 1:
                        #         finish = True
                        # if j_2 < j:
                        #     if field[i][j - 1] == 1:
                        #         start = True
                        #     if field[i][j_2 + 1] == 1:
                        #         finish = True
                        # if j_2 > j:
                        #     if field[i][j + 1] == 1:
                        #         start = True
                        #     if field[i][j_2 - 1] == 1:
                        #         finish = True
                        # if d[i * m + j] - d[i_2 * m + j_2] >= abs(i - i_2) + abs(j - j_2):
                        #     c = d[i * m + j] - d[i_2 * m + j_2] - abs(i - i_2) - abs(j - j_2)
                        #     if c not in ch:
                        #         ch[c] = 1
                        #     else:
                        #         ch[c] += 1
                        if d[i * m + j] - d[i_2 * m + j_2] >= 100 + abs(i - i_2) + abs(j - j_2):
                            cheats.add((i * m + j, i_2 * m + j_2))

print(len(cheats))
print(ch)