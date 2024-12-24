import math
def combo(line):
    line = line.strip().split()
    x = line[-2][2:-1]
    y = line[-1][2:]
    return int(x), int(y)


def min_sol(a_x, a_y, b_x, b_y, x, y):
    # k, m = crammers(a_x, a_y, b_x, b_y, x, y)
    if (a_y * x - a_x * y) % (a_y * b_x - a_x * b_y) == 0:
        m = (a_y * x - a_x * y) // (a_y * b_x - a_x * b_y)
        if (x - b_x * m) % a_x != 0:
            return 0
        k = (x - b_x * m) // a_x
        return k * 3 + m
    return 0


    # l1 = math.lcm(a_x, b_x)
    # p = l1 // a_x
    # q = l1 // b_x
    # assert a_x * p == b_x * q
    # if a_y * p != b_y * q:
    #     return k * 3 + m
    # print(p, q)
    # g = math.gcd(p, q)
    # p //= g
    # q //= g
    # if p * 3 > q:
    #     d = (m // q)
    #     k += p * d
    #     m -= d * q
    # elif p * 3 < q:
    #     d = (k // p)
    #     m += q * d
    #     k -= d * p
    # return k * 3 + m
#
# def crammers(a_x, a_y, b_x, b_y, x, y):
#     d = a_x * b_y - b_x * a_y
#     d_1 = x * b_y - b_x * y
#     d_2 = a_x * y - x * a_y
#     if d_1 % d == 0:
#         k = d_1 // d
#         m = d_2 // d
#         return k, m
#     else:
#         return -1, -1


f = open('input.txt', 'r')
lines = f.read().splitlines()
n = len(lines)
cnt = 0
j = 0
for i in range(0, n, 4):
    a = lines[i]
    b = lines[i+1]
    c = lines[i+2]
    a_x, a_y = combo(a)
    b_x, b_y = combo(b)
    x, y = combo(c)

    s = min_sol(a_x, a_y, b_x, b_y, 10000000000000 + x, 10000000000000 + y)
    print(s)
    cnt += s
    j += 1
    # cnt += min_sol(a_x, a_y, b_x, b_y, x, y)

print(cnt)
print(j)