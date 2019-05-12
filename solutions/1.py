def sum_of_multiplies(n):
    multiplies = set()
    for i in range(n):
        if i % 3 == 0:
            multiplies.add(i)
        if i % 5 == 0:
            multiplies.add(i)
    return sum(multiplies)

print sum_of_multiplies(1000)
