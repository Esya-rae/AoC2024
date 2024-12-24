MOD = 16777216


def compute_prices(secret, n):
    prices = [secret % 10]
    for i in range(n):
        secret = secret ^ (secret * 64)
        secret = secret % MOD
        secret = secret ^ (secret // 32)
        secret = secret % MOD
        secret = secret ^ (secret * 2048)
        secret = secret % MOD
        prices.append(secret % 10)
    return prices


def compute_seqs(prices):
    global bananas
    d = set()
    for i in range(1, len(prices) - 3):
        ch = []
        ch.append(prices[i] - prices[i - 1])
        ch.append(prices[i + 1] - prices[i])
        ch.append(prices[i + 2] - prices[i + 1])
        ch.append(prices[i + 3] - prices[i + 2])
        if tuple(ch) not in d:
            d.add(tuple(ch))
            if tuple(ch) not in bananas:
                bananas[tuple(ch)] = prices[i + 3]
            else:
                bananas[tuple(ch)] += prices[i + 3]


f = open('input.txt', 'r')
lines = f.read().splitlines()
cnt = 0
bananas = dict()
for line in lines:
    x = int(line)
    prices = compute_prices(x, 2000)
    compute_seqs(prices)

max_key = -1
max_value = 0
for key, value in bananas.items():
    if value > max_value:
        max_key = key
        max_value = value
print(max_value, max_key)