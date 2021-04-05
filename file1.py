import math


def fract(num):
    return num - int(num)


def rec(rem, sum=0):
    if fract(rem) == 0:
        return sum, rem
    else:
        upp = rem * 10
        sum = sum + int(upp)
        rem = fract(upp)
        return rec(sum, rem)


def fract_part(num):
    if num < 0:
        math.sqrt(num**2)
    result = fract(num)
    return result.imag  # is imag is second part?


inp = float(input())
result = fract_part(inp)
print(result)
