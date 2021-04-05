tup = tuple

for s in input():
    if tup.__contains__(tup, s):
        print("Yes")
    else:
        print("No")
    tup.__add__(tup, s)

