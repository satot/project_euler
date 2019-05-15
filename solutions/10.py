def find_primes(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return sum(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True

print find_primes(2000000)
