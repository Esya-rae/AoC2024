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


def to_dir_coord(x):
    if x == 'A':
        return 0, 2
    elif x == '^':
        return 0, 1
    elif x == '>':
        return 1, 2
    elif x == '<':
        return 1, 0
    else:
        return 1, 1

def dir_is_valid(x, seq):
    c_i, c_j = to_dir_coord(x)
    k = 0
    while k < len(seq) and (c_i != 0 or c_j != 0):
        if seq[k] == '^':
            c_i -= 1
        elif seq[k] == 'v':
            c_i += 1
        elif seq[k] == '<':
            c_j -= 1
        else:
            c_j += 1
        k += 1
    return k == len(seq) and (c_i != 0 or c_j != 0)


def dir_options(x, y):
    x_i, x_j = to_dir_coord(x)
    y_i, y_j = to_dir_coord(y)
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
        if dir_is_valid(x, oo):
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

def dir_options_global(seq): #seq should end with A
    os = []
    if len(seq) > 0:
        os.append(dir_options('A', seq[0]))
        if len(seq) > 1:
            os.append(dir_options(seq[0], seq[1]))
            if len(seq) > 2:
                os.append(dir_options(seq[1], seq[2]))
                if len(seq) > 3:
                    os.append(dir_options(seq[2], seq[3]))
                    if len(seq) > 4:
                        os.append(dir_options(seq[3], seq[4]))
    # print(os)
    op = set([''])
    for i in range(len(os)):
        op_new = set()
        for j in op:
            for k in os[i]:
                op_new.add(j + k + 'A')
        op = op_new.copy()
    # print(list(op))
    return op

def best_option_calc(seq):
    global best_options
    if seq in best_options:
        return best_options[seq]
    op = dir_options_global(seq)
    op_new = set()
    # print('SEQ', seq)
    for o in op:
        s = o.split('A')
        c = ''
        # print(s)
        for k in s[:-1]:
            # print(k)
            opp = dir_options_global(k + 'A')
            # print('opp', opp)
            for h in opp:
                c += h
                break
            # print('c', c)
        op_new.add(c)
        # print('op_new', op_new)
    res = ''
    res_l = 1000000000000
    for o in op_new:
        if len(o) < res_l:
            res = o
            res_l = len(o)
    best_options[seq] = res
    return res


f = open('input.txt', 'r')
lines = f.read().splitlines()
best_options = dict()
cnt = 0
for line in lines:
    line = line.strip()
    # if line == '456A':
    no = num_options_global(line)
    l = 10000000000
    f_enc = ''
    for num_op in no:
        no_0 = num_op.split('A')
        enc = ''
        for i in no_0[:-1]:
            enc += best_option_calc(i + 'A')
        if len(enc) < l:
            l = len(enc)
            f_enc = enc
    print(f_enc, len(f_enc))
    cnt += len(f_enc) * int(line[:-1])

    # break

print(best_options)
print(cnt)