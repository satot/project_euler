def find_palindrome(n):
    result = []
    for i in xrange(n, 99, -1):
        for j in xrange(i, 99, -1):
            if "".join(reversed(str(i*j))) == str(i*j):
                result.append(i*j)
    return max(result)

print find_palindrome(999)
