def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            return [i] + prime_factors(n//i)
    return [n]

def countup(primes):
    memo = dict()
    for n in primes:
        if n in memo:
            memo[n] += 1
        else:
            memo[n] = 1
    formatted = set()
    for k in memo:
        formatted.add((k, memo[k]))
    return formatted

def add(res, primes):
    for p in primes:
        n, cnt = p[0], p[1]
        for r in res:
            if r[0] == n and r[1] < cnt:
                res.remove(r)
                res.add(p)
    return res

def evenly_divisible(n):
    result = set()
    for i in range(1, n+1):
        if is_prime(i):
            result.add((i, 1))
        else:
            prims = countup(prime_factors(i))
            if prims in result:
                continue
            else:
                result = add(result, prims)
    prod = 1
    print result
    for i in result:
        prod *= i[0] ** i[1]
    return prod

print evenly_divisible(10)
print evenly_divisible(20)
