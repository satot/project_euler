def memoize(f):
    cache = dict()
    def helper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return helper

@memoize
def factorial(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

def find_nth_permutation(n, length):
    res = []
    tmp = 0
    for i in range(1, length+1):
        for j in range(1, length+1):
            if j * factorial(length-i) + tmp > n:
                res.append(j-1)
                tmp += (j-1) * factorial(length-i)
                break
    return res

def lexicographic_permutation(digits, n):
    d = list(digits) # copy of list (python2)
    p = ""
    for i in find_nth_permutation(n-1, len(d)):
        p += d.pop(i)
    return p

digits = list('012')
n = 2
assert lexicographic_permutation(digits, n) == "021"
n = 3
assert lexicographic_permutation(digits, n) == "102"
n = 6
assert lexicographic_permutation(digits, n) == "210"

digits = list('0123456789')
n = 1000000
print lexicographic_permutation(digits, n)
