def is_okay(s):
    global patterns
    x = [0] * (len(s) + 1)
    x[0] = 1
    for i in range(1, len(s) + 1):
        for j in range(i):
            if s[j:i] in patterns and x[j] > 0:
                x[i] += x[j]
    return x[-1]


f = open('input.txt', 'r')
lines = f.read().splitlines()
n = len(lines)

p = lines[0]
patterns = set(p.split(', '))
cnt = 0
for i in range(2, n):
    s = lines[i].strip()
    cnt += is_okay(s)

print(cnt)