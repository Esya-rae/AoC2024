from itertools import product

def c2i(x):
    return (ord(x[0]) - ord('a')) * num_letters + ord(x[1]) - ord('a')

def i2c(x):
    return chr((x // num_letters) + ord('a')) + chr((x % num_letters) + ord('a'))

def is_clique(x):
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[j] == x[i] or x[j] not in g[x[i]]:
                return False
    return True


def find_cliques(potential_clique=[], remaining_nodes=[], skip_nodes=[], depth=0):
    global max_clique
    if len(potential_clique) > len(max_clique):
        max_clique = potential_clique.copy()

    if len(remaining_nodes) == 0 and len(skip_nodes) == 0:
        return

    for node in remaining_nodes:
        new_potential_clique = potential_clique + [node]
        new_remaining_nodes = [n for n in remaining_nodes if n in g[node]]
        new_skip_list = [n for n in skip_nodes if n in g[node]]
        find_cliques(new_potential_clique, new_remaining_nodes, new_skip_list, depth + 1)
        remaining_nodes.remove(node)
        skip_nodes.append(node)


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

max_clique = []
find_cliques(remaining_nodes=list(range(num_letters ** 2)))
print(max_clique)
res = []
for i in range(len(max_clique)):
    res.append(i2c(max_clique[i]))
res.sort()
print(','.join(res))