def is_ordered(x):
    global g
    for i in range(len(x) - 1):
        for j in range(i + 1, len(x)):
            if x[i] in g[x[j]]:
                return False
    return True

def order(x):
    global g
    res = []
    rem = x.copy()
    while len(rem) > 0:
        for i in range(len(rem)):
            c = 0
            for j in range(len(rem)):
                if rem[i] in g[rem[j]]:
                    break
                c += 1
            if c == len(rem):
                a = rem.pop(i)
                res.append(a)
                break
    return res



f = open('input.txt', 'r')
lines = f.readlines()
g = [[] for _ in range(100)]
ind = 0
for line in lines:
    if len(line) < 4 or line[2] != '|':
        break
    v, w = line.split('|')
    g[int(v)].append(int(w))
    ind += 1

cnt = 0
for i in range(ind + 1, len(lines)):
    x = list(map(int, lines[i].split(',')))
    # print(x)
    if not is_ordered(x):
        res = order(x)
        cnt += res[len(res)// 2]
print(cnt)







