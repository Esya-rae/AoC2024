
def is_safe(x, inc):
    for i in range(len(x) - 1):
        if (inc and x[i] >= x[i + 1]) or (abs(x[i + 1] - x[i]) > 3) or (not inc and x[i] <= x[i + 1]):
            return False
    return True
def is_safe_err(x, inc):
    print(x, inc)
    print(x[1:])
    if is_safe(x[1:], inc):
        return True
    print(x[:len(x) - 1])
    if is_safe(x[:len(x) - 1], inc):
        return True
    for j in range(1, len(x) - 1):
        y = x[0:j].copy()
        y.extend(x[j + 1:])
        print(y)
        if is_safe(y, inc):
            return True
    return False



f = open('input.txt', 'r')
lines = f.readlines()
c = 0
for line in lines:
    x = list(map(int, line.strip().split()))
    print(x)
    if is_safe_err(x, True) or is_safe_err(x, False):
        print('safe')
        c += 1
print(c)