def find_amicables(n):
    amicables = set()
    for i in range(2, n+1):
        s1 = d(i)
        if s1 == i:
            continue
        s2 = d(s1)
        if s2 == i:
            print i, s1
            amicables.add(i)
            amicables.add(s1)
    return amicables

def memoize(f):
    cache = dict()
    def helper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return helper

@memoize
def d(n):
    divs = set()
    for i in range(1, n//2+1):
        if n % i == 0:
            divs.add(i)
    return sum(divs)

ami = find_amicables(10000)
print ami
print sum(ami)
