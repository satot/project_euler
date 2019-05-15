def find_pythagorean(n):
    for c in xrange(n-1, 1, -1):
        for a in range(1, c):
            b = n - c - a
            if b <= 0:
                break
            if a ** 2 + b ** 2 == c ** 2:
                return a*b*c
    return None


def is_int(n):
    return n == int(n)

print find_pythagorean(1000)
