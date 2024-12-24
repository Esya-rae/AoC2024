def transform(line):
    res = []
    for i in range(len(line)):
        if i % 2 == 1:
            for j in range(int(line[i])):
                res.append(-1)
        else:
            for j in range(int(line[i])):
                res.append(i // 2)
    return res


f = open('input.txt', 'r')
line = f.readline().strip()
n = len(line)


cnt = 0
i = 0
res = transform(line)
# print(res)
j = len(res) - 1

while i < j:
    if res[i] == -1:
        while j > i and res[j] == -1:
            j -= 1
        if j == i:
            break
        cnt += res[j] * i
        # print(j, i, res[j], res[j] * i)
        j -= 1
    else:
        cnt += res[i] * i
        # print(i, res[i] * i)
    i += 1

if res[i] != -1:
    cnt += res[i] * i

print(cnt)