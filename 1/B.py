f = open('input.txt', 'r')
lines = f.readlines()
x = []
y = []
for line in lines:
    a, b = map(int, line.split())
    x.append(a)
    y.append(b)
x.sort()
y.sort()
sim = 0
c = 0
j = 0
i = 0
while i < len(x):
    m = 1
    while i + m < len(x) and x[i] == x[i + m]:
        m += 1
    i += (m - 1)
    c = 0
    while y[j] < x[i]:
        j += 1
    while y[j] == x[i]:
        c += 1
        j += 1
    sim += x[i] * c * m
    i += 1
print(sim)