def nth_prime(n):
    cnt = 0
    i = 2
    while True:
        if is_prime(i):
            cnt += 1
            if cnt == n:
                break
        i += 1
    return i

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print nth_prime(6)
print nth_prime(10001)
