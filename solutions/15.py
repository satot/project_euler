from math import factorial as fc
def fastest_route(m, n):
    return fc(m+n)/(fc(m)*fc(n))

print fastest_route(20,20)
