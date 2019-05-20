def is_abundant(n):
    divs = set()
    for i in range(1, n//2+1):
        if n % i == 0:
            divs.add(i)
    return sum(divs) > n

def find_abundant(n):
    abds = set()
    for i in range(n):
        if is_abundant(i):
            abds.add(i)
    return abds

def non_abundant_sums(n):
    abds = find_abundant(n)
    target = set()
    for i in range(1, n):
        can = False
        for j in range(1, i//2+1):
            if j in abds and (i-j) in abds:
                can = True
                break
        if not can:
            target.add(i)
    return target

#print find_abundant(100)
nas = non_abundant_sums(30000)
print nas
print sum(nas)
print max(nas)
