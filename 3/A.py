f = open('input.txt', 'r')
lines = f.readlines()
c = 0
res = 0
add = True
for line in lines:
    i = 0
    n = len(line)
    # print(line)
    while i < n:
        # if i < n - 6:
        #     print(line[i:i+4], line[i:i+6], line[i:i+3])
        if i < n - 4 and line[i:i + 4] == 'do()':
            add = True
            i += 4
        elif i < n - 7 and line[i:i + 7] == 'don\'t()':
            add = False
            i += 7
        elif i < n - 2 and line[i:i+3] == "mul":
            i += 3
            if line[i] != '(':
                i += 1
                continue
            i += 1
            a = ''
            while i < n and '0' <= line[i] <= '9':
                a += line[i]
                i += 1
            if line[i] != ',':
                i += 1
                continue
            i += 1
            b = ''
            while i < n and '0' <= line[i] <= '9':
                b += line[i]
                i += 1
            if line[i] != ')':
                i += 1
                continue
            if 0 < len(a) <= 3 and 0 < len(b) <= 3:
                if add:
                    res += int(a) * int(b)
            i += 1
        else:
            i += 1
    # break
print(res)