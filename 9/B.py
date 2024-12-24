def transform(line):
    res = []
    for i in range(len(line)):
        if i % 2 == 1:
            res.append((-1, int(line[i])))
        else:
            res.append((i // 2, int(line[i])))
    return res

def transform_2(res):
    x = res.copy()
    for i in range((len(res)) // 2,0, -1):
        k = 0
        # print(i)
        while x[k][0] != i:
            k += 1
        j = 0
        while j < k:
            if x[j][0] == -1 and x[j][1] >= x[k][1]:
                x_new = x[:j]
                x_new.append(x[k])
                if x[j][1] > x[k][1]:
                    x_new.append((-1, x[j][1] - x[k][1]))
                # print('x', x)
                x_new.extend(x[j+1:k])
                x_new.append((-1, x[k][1]))
                x_new.extend(x[k+1:])
                # print('x_new', x_new)
                x_new = congest(x_new)
                x = x_new.copy()
                # print(x)
                break
            j += 1
    return x

def congest(x):
    r = []
    i = 0
    # print(x)
    while i < len(x):
        if x[i][0] != -1:
            r.append(x[i])
            # print(x[i])
            i += 1
        else:
            k = 0
            # print('start')
            while i < len(x) and x[i][0] == -1:
                # print(x[i])
                k += x[i][1]
                i += 1
            # print('end')
            r.append((-1, k))
    return r




f = open('input.txt', 'r')
line = f.readline().strip()
n = len(line)


cnt = 0
i = 0
res = transform(line)
# print(res)
x = transform_2(res)
# print(x)
k = 0

for i in range(len(x)):
    if x[i][0] == -1:
        k += x[i][1]
    else:
        for j in range(x[i][1]):
            cnt += x[i][0] * k
            k += 1
    # print(cnt)

print(cnt)