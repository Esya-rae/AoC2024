def is_safe(x, inc):
    i = 0
    err = 0
    while i < len(x) - 1:
        if (inc and x[i] >= x[i + 1]) or (abs(x[i + 1] - x[i]) > 3) or (not inc and x[i] <= x[i + 1]):
            if i == 0 or i == len(x) - 2:
                err += 1
                i += 1
            elif (inc and x[i] >= x[i + 2]) or (abs(x[i + 1] - x[i]) > 3) or (not inc and x[i] <= x[i + 2]):
                err += 1
                i += 2
            else:
                return False
        if err > 1:
            return False
        i += 1
    return True


f = open('input.txt', 'r')
lines = f.readlines()
c = 0
for line in lines:
    x = list(map(int, line.strip().split()))
    print(x)
    if is_safe(x, True) or is_safe(x, False):
        print('safe')
        c += 1
print(c)