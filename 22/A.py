MOD = 16777216


def compute_nth(secret, n):
    for i in range(n):
        secret = secret ^ (secret * 64)
        secret = secret % MOD
        secret = secret ^ (secret // 32)
        secret = secret % MOD
        secret = secret ^ (secret * 2048)
        secret = secret % MOD
    return secret



f = open('input.txt', 'r')
lines = f.read().splitlines()
cnt = 0
for line in lines:
    x = int(line)
    cnt += compute_nth(x, 2000)
print(cnt)

#print(compute_nth(1, 2000))