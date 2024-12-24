def is_safe_inc(x, inc):
    i = 0
    errors = 0
    while i < len(x) - 1:
        if (inc and x[i] >= x[i + 1]) or (abs(x[i + 1] - x[i]) > 3) or (not inc and x[i] <= x[i + 1]):
            return False
        if errors > 2:
            return False
        i += 1
    return errors <= 2



f = open('input.txt', 'r')
lines = f.readlines()
c = 0
for line in lines:
    x = list(map(int, line.strip().split()))
    if is_safe(x):
        c += 1
print(c)