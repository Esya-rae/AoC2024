def path_num(x, y, flag=False):
    r = ''
    if not flag:
        if (x + 1) % 3 > (y + 1) % 3:
            r += '<'*((x + 1) % 3 - (y + 1) % 3)
        else:
            r += '>'*((y + 1) % 3 - (x + 1) % 3)
    if 2 - (x - 1) // 3 > 2 - (y - 1) // 3:
        r += '^'*((y - 1) // 3 - (x - 1) // 3)
    else:
        r += 'v'*((x - 1) // 3 - (y - 1) // 3)
    if flag:
        if (x + 1) % 3 > (y + 1) % 3:
            r += '<'*((x + 1) % 3 - (y + 1) % 3)
        else:
            r += '>'*((y + 1) % 3 - (x + 1) % 3)
    return r

def num_presses(code):
    seq = ''
    prev = 'A'
    print(code)
    for i in range(0, len(code)):
        cur = code[i]
        if cur == prev:
            seq += 'A'
        elif cur in '0A' and prev in '0A':
            if cur == '0':
                seq += '<A'
            else:
                seq += '>A'
        elif prev in '0A':
            if prev == '0':
                seq += '^' + path_num(2, int(cur), flag=True) + 'A'
            else:
                seq += '^' + path_num(3, int(cur), flag=True) + 'A'
        elif cur in '0A':
            if cur == '0':
                seq += path_num(int(prev), 2) + 'v' + 'A'
            else:
                seq += path_num(int(prev), 3) + 'v' + 'A'
        else:
            seq += path_num(int(prev), int(cur)) + 'A'
        prev = cur
    return seq


def dir_presses(code):
    seq = ''
    prev = 'A'
    d = {'<': 0, '>': 2, 'v': 1}
    for i in range(0, len(code)):
        cur = code[i]
        if cur == prev:
            seq += 'A'
        elif cur in '^A' and prev in '^A':
            if prev == 'A':
                seq += '<A'
            else:
                seq += '>A'
        elif prev in '^A':
            if prev == 'A':
                seq += 'v' + '<' * (d['>'] - d[cur]) + 'A'
            else:
                if cur == '>':
                    seq += 'v>A'
                elif cur == '<':
                    seq += 'v<A'
                else:
                    seq += 'vA'
        elif cur in '^A':
            if cur == 'A':
                seq += '>' * (d['>'] - d[prev]) + '^' + 'A'
            else:
                if prev == '>':
                    seq += '<^A'
                elif prev == '<':
                    seq += '>^A'
                else:
                    seq += '^A'
        else:
            if d[cur] > d[prev]:
                seq += '>' * (d[cur] - d[prev]) + 'A'
            else:
                seq += '<' * (d[prev] - d[cur]) + 'A'
        prev = cur

    return seq


f = open('test.txt', 'r')
lines = f.read().splitlines()
for line in lines:
    if line.strip() == '456A':
        seq_1 = num_presses(line.strip())
        print(seq_1)
        seq_2 = dir_presses(seq_1)
        print(seq_2)
        seq_3 = dir_presses(seq_2)
        print(seq_3)
        print(len(seq_3))