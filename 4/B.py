def is_xmas(a, b, c, d, e):
    if b != 'A':
        return False
    if not ((a == 'M' and c == 'S') or (a == 'S' and c == 'M')):
        return False
    if not ((d == 'M' and e == 'S') or (d == 'S' and e == 'M')):
        return False
    return True


f = open('input.txt', 'r')
lines = f.readlines()
res = 0
n = len(lines[0].strip())
for i in range(len(lines) - 2):
    for j in range(n - 2):
        if is_xmas(lines[i][j], lines[i + 1][j + 1], lines[i + 2][j + 2], lines[i + 2][j], lines[i][j + 2]):
            res += 1


print(res)