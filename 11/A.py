def num_stones(s, b):
    global x
    if (s, b) in x:
        return x[(s, b)]
    if b == 0:
        x[(s, b)] = 1
        return x[(s, b)]
    if s == 0:
        x[(s, b)] = num_stones(1, b - 1)
        return x[(s, b)]
    if len(str(s)) % 2 == 0:
        k = len(str(s)) // 2
        x[(s, b)] = num_stones(int(str(s)[:k]), b - 1) + num_stones(int(str(s)[k:]), b - 1)
        return x[(s, b)]
    x[(s, b)] = num_stones(s * 2024, b - 1)
    return x[(s, b)]


f = open('input.txt', 'r')
line = f.readline()
stones = list(map(int, line.split()))
x = dict()

cnt = 0
for c in stones:
    cnt += num_stones(c, 75)
    print(cnt)
print(cnt)