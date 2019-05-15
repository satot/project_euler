def sq_of_sum(n):
    return (n * (n+1) // 2)**2

def sum_of_sq(n):
    return sum([i**2 for i in range(n+1)])

n = 10
print sq_of_sum(n) - sum_of_sq(n)
n = 100
print sq_of_sum(n) - sum_of_sq(n)
