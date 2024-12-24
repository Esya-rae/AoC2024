def is_okay(r, s):
    for i in range(3 ** (len(s) - 1)):
        k = i
        m = s[0]
        for j in range(1, len(s)):
            if k % 3 == 0:
                m += s[j]
            elif k % 3 == 1:
                m *= s[j]
            else:
                ll = len(str(s[j]))
                m = m * (10 ** ll) + s[j]
            k //= 3
        if m == r:
            return True
    return False


f = open('input.txt', 'r')
lines = f.readlines()

cnt = 0
for line in lines:
    l = line.split(': ')
    r = int(l[0])
    s = list(map(int, l[1].split()))
    if is_okay(r, s):
        cnt += r
print(cnt)
