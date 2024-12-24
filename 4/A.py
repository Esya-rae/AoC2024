def is_xmas(a, b, c, d):
    if a == 'X' and b == 'M' and c == 'A' and d == 'S':
        return True
    if a == 'S' and b == 'A' and c == 'M' and d == 'X':
        return True
    return False


f = open('input.txt', 'r')
lines = f.readlines()
res = 0
for i in range(len(lines)):
    n = len(lines[i].strip())
    # print(i)
    for j in range(n):
        if j < len(lines[i]) - 4:
            if i < len(lines) - 3 and is_xmas(lines[i][j], lines[i + 1][j + 1], lines[i + 2][j + 2], lines[i + 3][j + 3]):
                res += 1
                # print('dr')
            if is_xmas(lines[i][j], lines[i][j + 1], lines[i][j + 2], lines[i][j + 3]):
                res += 1
                # print('h')
        if j >= 3 and i < len(lines) - 3 and is_xmas(lines[i][j], lines[i + 1][j - 1], lines[i + 2][j - 2], lines[i + 3][j - 3]):
            res += 1
            # print('dl')
        if i < len(lines) - 3 and is_xmas(lines[i][j], lines[i + 1][j], lines[i + 2][j], lines[i + 3][j]):
            res += 1
            # print('v')
print(res)