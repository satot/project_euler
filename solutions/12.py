from itertools import combinations

def dividors(n):
    i = 0
    tri = 0
    while True:
        i += 1
        tri += i
        if num_of_dividors(tri) >= n:
            return tri
        if i > 1000000:
            break
    return None

def get_primes(n):
    for i in range(2, int(n**0.5)+1):
        quot, remainder = divmod(n, i)
        if remainder == 0:
            return [i] + get_primes(quot)
    return [n]

def prod(numbers):
    prod = 1
    for n in numbers:
        prod *= n
    return prod

def num_of_dividors(n):
    primes = get_primes(n)
    divs = set()
    for i in range(1, len(primes)+1):
        for l in combinations(primes, i):
            divs.add(prod(l))
    return len(divs)

print dividors(500)
