def find_primes(n):
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            print n,i
            return [i] + find_primes(n/i)
    return [n]

n = 600851475143

print max(find_primes(n))
