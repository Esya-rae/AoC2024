def c2i(x):
    return (ord(x[0]) - ord('a')) * num_letters + ord(x[1]) - ord('a')

def idt(x):
    for i in range(3):
        if x[i] // num_letters == ord('T') - ord('A'):
            return True
    return False



num_letters = ord('Z') - ord('A') + 1

file = open('input.txt', 'r')
lines = file.readlines()
g = [[] for _ in range(num_letters ** 2)]

for line in lines:
    line = line.strip().split('-')

    x = line[0]
    y = line[1]
    g[c2i(x)].append(c2i(y))
    g[c2i(y)].append(c2i(x))

triangles = set()
for v in range(num_letters ** 2):
    for w in g[v]:
        for u in g[w]:
            if u != v and u in g[v]:
                t = [v, w, u]
                if idt(t):
                    triangles.add(tuple([v, w, u]))
print(len(triangles) // 6)