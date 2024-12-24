import math
from itertools import permutations

def to_num_coord(x):
    if x == 'A':
        c_i = 3
        c_j = 2
    elif x == '0':
        c_i = 3
        c_j = 1
    else:
        c_i = 2 - (int(x) - 1) // 3
        c_j = (int(x) - 1) % 3
    return c_i, c_j

def num_is_valid(x, seq):
    c_i, c_j = to_num_coord(x)
    k = 0
    while k < len(seq) and (c_i != 3 or c_j != 0):
        if seq[k] == '^':
            c_i -= 1
        elif seq[k] == 'v':
            c_i += 1
        elif seq[k] == '<':
            c_j -= 1
        else:
            c_j += 1
        k += 1
    return k == len(seq) and (c_i != 3 or c_j != 0)

def code_to_num(code):
    res = [0] * 25
    if len(code) > 0:
        res[buttons_to_num['A'] * 5 + buttons_to_num[code[0]]] += 1
    for i in range(len(code) - 1):
          x = buttons_to_num[code[i]] * 5 + buttons_to_num[code[i + 1]]
          res[x] += 1
    return res

def num_options(x, y):
    x_i, x_j = to_num_coord(x)
    y_i, y_j = to_num_coord(y)
    seq = ''
    if y_i > x_i:
        seq += 'v' * (y_i - x_i)
    else:
        seq += '^' * (x_i - y_i)
    if y_j > x_j:
        seq += '>' * (y_j - x_j)
    else:
        seq += '<' * (x_j - y_j)
    options = permutations(seq)
    v = set()
    for o in options:
        oo = ''.join(o)
        if num_is_valid(x, oo):
            v.add(oo)
    return v

def num_options_global(code):
    o1 = num_options('A', code[0])
    o2 = num_options(code[0], code[1])
    o3 = num_options(code[1], code[2])
    o4 = num_options(code[2], code[3])
    # print(o1, o2, o3, o4)

    op = []
    for i1 in o1:
        for i2 in o2:
            for i3 in o3:
                for i4 in o4:
                    op.append(i1 + 'A' + i2 + 'A' + i3 + 'A' + i4 + 'A')
    # print(op)
    return op


def paths(a, b):
    if a == '^':
        if b == '^':
            return []
        elif b == 'A':
            return ['>']
        elif b == '<':
            return ['v<']
        elif b == 'v':
            return ['v']
        else:
            return ['>v', 'v>']
    elif a == 'A':
        if b == '^':
            return ['<']
        elif b == 'A':
            return []
        elif b == '<':
            return ['v<<', '<v<']
        elif b == 'v':
            return ['<v', 'v<']
        else:
            return ['v']
    elif a == '<':
        if b == '^':
            return ['>^']
        elif b == 'A':
            return ['>^>', '>>^']
        elif b == '<':
            return []
        elif b == 'v':
            return ['>']
        else:
            return ['>>']
    elif a == 'v':
        if b == '^':
            return ['^']
        elif b == 'A':
            return ['^>', '>^']
        elif b == '<':
            return ['<']
        elif b == 'v':
            return []
        else:
            return ['>']
    else:
        if b == '^':
            return ['<^', '^<']
        elif b == 'A':
            return ['^']
        elif b == '<':
            return ['<<']
        elif b == 'v':
            return ['<']
        else:
            return []

def combo_to_num(c):
    return buttons_to_num[c[0]] * 5 + buttons_to_num[c[1]]



dist = dict()
buttons = ['^', 'A', '<', 'v', '>']
buttons_to_num = dict(zip(buttons, range(len(buttons))))
arrow_pad = [['', '^', 'A'], ['<', 'v', '>']]

dists = [1] * 25
for a in buttons:
    for b in buttons:
        ps = paths(a, b)
        if len(ps) > 0:
            dists[buttons_to_num[a] * 5 + buttons_to_num[b]] = len(ps[0]) + 1


for i in range(24):
    dists_new = [math.inf] * 25
    for a in buttons:
        for b in buttons:
            ps = paths(a, b)
            x = buttons_to_num[a] * 5 + buttons_to_num[b]
            if len(ps) == 0:
                dists_new[x] = 1
            else:
                for p in ps:
                    p = 'A' + p + 'A'
                    d = 0
                    for i in range(len(p) - 1):
                        d += dists[combo_to_num(p[i] + p[i + 1])]
                    dists_new[x] = min(dists_new[x], d)
    dists = dists_new.copy()


f = open('input.txt', 'r')
lines = f.read().splitlines()
res = 0
for line in lines:
    final_ans = math.inf
    no = num_options_global(line)
    for op in no:
        ans = 0
        num = code_to_num(op)
        for i in range(25):
            ans += dists[i] * num[i]
        final_ans = min(final_ans, ans)
    res += int(line[:-1]) * final_ans
print(res)


