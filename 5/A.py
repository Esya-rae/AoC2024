def topological_sort_dfs(v):
    global result, G, visited
    visited[v] = True

    for w in g[v]:
        if not visited[w]:
            topological_sort_dfs(w)

    result.append(v)

def is_ordered(x):
    global ordering
    for i in range(len(x) - 1):
        if ordering[x[i]] > ordering[x[i + 1]]:
            return False
    return True



f = open('test.txt', 'r')
lines = f.readlines()
g = [[] for _ in range(100)]
result = []
minn = 100
maxx = 0
ind = 0
for line in lines:
    if len(line) < 4 or line[2] != '|':
        break
    v, w = line.split('|')
    g[int(v)].append(int(w))
    minn = min(minn, int(v))
    minn = min(minn, int(w))
    maxx = max(maxx, int(v))
    maxx = max(maxx, int(w))
    ind += 1

visited = [False] * 100

for v in range(100):
    if not visited[v]:
        topological_sort_dfs(v)

ordering = dict()
for i in range(len(result)):
    ordering[result[i]] = i

cnt = 0
for i in range(ind + 1, len(lines)):
    x = list(map(int, lines[i].split(',')))
    print(x)
    if is_ordered(x):
        print(x)
        cnt += x[len(x) // 2 + 1]
print(cnt)







