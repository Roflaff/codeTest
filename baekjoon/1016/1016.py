import math

# 입력 받기
min_val, max_val = map(int, input().split())
total = max_val - min_val + 1

# 전체 수를 True로 설정
X = [True] * total

# 2부터 sqrt(max_val)까지의 소수 구하기
is_prime = [True] * (int(math.sqrt(max_val)) + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(math.sqrt(max_val)) + 1):
    if is_prime[i]:
        for j in range(i * i, len(is_prime), i):
            is_prime[j] = False

primes = [i for i in range(2, len(is_prime)) if is_prime[i]]
print(primes)

# 각 소수의 제곱수로 나누어지는 수를 제외하기
for prime in primes:
    prime_square = prime * prime
    # min_val 부터 max_val까지 범위에서 prime_square로 나누어지는 수를 제외
    start = max(prime_square, (min_val + prime_square - 1) // prime_square * prime_square)
    for i in range(start, max_val + 1, prime_square):
        X[i - min_val] = False

# 최종적으로 X에서 True인 값의 개수를 출력
count = sum(X)
print(count)
