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
dif = 0
for i in range(len(x)):
    dif += abs(x[i] - y[i])
print(dif)