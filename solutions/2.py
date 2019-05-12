def memoize(f):
    cache = dict()
    def helper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return helper

@memoize
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    s = 0
    i = 0
    while fib(i) <= 4000000:
        if fib(i) % 2 == 0:
            s += fib(i)
        i += 1
    print s

