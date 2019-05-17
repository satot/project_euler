def memoize(f):
    cache = dict()
    def helper(n):
        if not n in cache:
            cache[n] = f(n)
        return cache[n]
    return helper

@memoize
def calc_length(n):
    length = 0
    while not n == 1:
        print n
        length += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
    return length

def find_longest_collats2(n):
    longest_length = 0
    longest_start = 0
    for i in range(2, n+1):
        length = calc_length(i)
        if length > longest_length:
            longest_length = length
            longest_start = i
    return longest_start, longest_length

#print find_longest_collats2(1000000)
calc_length(837799)
