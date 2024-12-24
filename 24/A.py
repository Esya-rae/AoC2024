from collections import deque

def to_z(i):
    if i < 10:
        i = '0' + str(i)
    else:
        i = str(i)
    return 'z' + i


def to_x(i):
    if i < 10:
        i = '0' + str(i)
    else:
        i = str(i)
    return 'x' + i


def to_y(i):
    if i < 10:
        i = '0' + str(i)
    else:
        i = str(i)
    return 'y' + i


def and_2(a, b):
    global clauses_2
    if tuple([a, 'AND', b]) in clauses_2:
        return tuple([a, 'AND', b])
    elif tuple([b, 'AND', a]) in clauses_2:
        return tuple([b, 'AND', a])
    return False


def xor_2(a, b):
    global clauses_2
    if tuple([a, 'XOR', b]) in clauses_2:
        return tuple([a, 'XOR', b])
    elif tuple([b, 'XOR', a]) in clauses_2:
        return tuple([b, 'XOR', a])
    return False


def or_2(a, b):
    global clauses_2
    if tuple([a, 'OR', b]) in clauses_2:
        return tuple([a, 'OR', b])
    elif tuple([b, 'OR', a]) in clauses_2:
        return tuple([b, 'OR', a])
    return False

def swap(a, b):
    c1 = clauses_par[a]
    c2 = clauses_par[b]
    clauses_par[a], clauses_par[b] = c2, c1
    clauses_2[c1] = b
    clauses_2[c2] = a
    swaps.append(a)
    swaps.append(b)

def is_okay(a, b, c, i):
    zi = to_z(i)
    h1 = clauses_2[xor_2(a, b)]
    if xor_2(c, h1):
        hh = clauses_2[xor_2(c, h1)]
        if hh != zi:
            print('SWAP', hh, zi)
            swap(hh, zi)
    else:
        cc0 = clauses_par[to_z(i)]
        if c == cc0[2]:
            h0 = cc0[0]
        elif c == cc0[0]:
            h0 = cc0[2]
        else:
            print('WEIRD')
        print('SWAP', h1, h0)
        swap(h1, h0)
        h1 = h0
    h2 = clauses_2[and_2(a, b)]
    if and_2(h1, c):
        h3 = clauses_2[and_2(h1, c)]
        if or_2(h3, h2):
            h4 = clauses_2[or_2(h3, h2)]
            return h4
        else:
            print('unpredictable wrong, or')
    else:
        print('unpredictable wrong, and')


f = open('input.txt', 'r')
lines = f.readlines()
n = len(lines)

values = dict()
clauses = dict()
clauses_2 = dict()
clauses_vars = dict()
clauses_par = dict()
first_part = True
x_val = 0
y_val = 0

for i in range(n):
    if len(lines[i]) <= 1:
        first_part = False
    elif first_part:
        x = lines[i].split(': ')
        values[x[0]] = int(x[1])
        if x[0][0] == 'x':
            x_val += 2 ** int(x[0][1:]) * int(x[1])
        elif x[0][0] == 'y':
            y_val += 2 ** int(x[0][1:]) * int(x[1])
    else:
        x = lines[i].split()
        clauses[x[4]] = tuple([x[0], x[1], x[2]])
        clauses_2[tuple([x[0], x[1], x[2]])] = x[4]
        if x[0] not in clauses_vars:
            clauses_vars[x[0]] = [tuple([x[0], x[1], x[2]])]
        else:
            clauses_vars[x[0]].append(tuple([x[0], x[1], x[2]]))
        if x[2] not in clauses_vars:
            clauses_vars[x[2]] = [tuple([x[0], x[1], x[2]])]
        else:
            clauses_vars[x[2]].append(tuple([x[0], x[1], x[2]]))
        clauses_par[x[4]] = tuple([x[0], x[1], x[2]])

helping_vars = []
swaps = []
helping_vars.append(clauses_2[and_2('x00', 'y00')])
for i in range(1, 45):
    x, y = to_x(i), to_y(i)
    h4 = is_okay(x, y, helping_vars[-1], i)
    if h4:
        helping_vars.append(h4)

swaps.sort()
print(*swaps, sep=',')