def tuptup():
    tup = tuple()

    for s in input():
        if tup.__contains__(s):
            print("Yes")
        else:
            print("No")
        tup.__put__(s)


tuptup()