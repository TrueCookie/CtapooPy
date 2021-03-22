def powerList(list, power):
    return [pow(a, power) for a in list]


a = [56, 24, 56, 258, 2, 138]
minA = min(a)
print(minA)

b = powerList(a, minA)
maxB = max(b)
print(maxB)

