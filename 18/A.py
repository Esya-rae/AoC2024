import math
import heapq
from collections import deque


def dijkstra():
    global graph, x, y
    start = 0
    # print(start)
    size = 71 * 71
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


f = open('input.txt', 'r')
lines = f.read().splitlines()
nn = len(lines)

for k in range(1024, nn):
    field = [[0 for _ in range(71)] for _ in range(71)]

    for i in range(k):
        x, y = map(int, lines[i].strip().split(','))
        field[x][y] = 1

    graph = [[] for i in range(71*71)]
    n, m = 71, 71
    for i in range(71):
        for j in range(71):
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
    if d[-1] == float('inf'):
        print(lines[k - 1])
        break
