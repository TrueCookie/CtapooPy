def app_flag(flag1, flag2):
    # change flag (change direction)
    if not flag1 and not flag2:
        flag1 = 0
        flag2 = 1
    elif not flag1 and flag2:
        flag1 = 1
        flag2 = 0
    elif flag1 and not flag2:
        flag1 = 1
        flag2 = 1
    elif flag1 and flag2:
        flag1 = 0
        flag2 = 0
    return flag1, flag2


def app_marker(i, j, flag1, flag2):
    if not flag1 and not flag2:  # 00
        j = j + 1
    elif not flag1 and flag2:   # 01
        i = i + 1
    elif flag1 and not flag2:   # 10
        j = j - 1
    elif flag1 and flag2:   # 11
        i = i - 1
    return i, j


def print_snail(n):
    list0 = [[0 for j in range(n)] for i in range(n)]
    i = 0
    j = 0
    count = 1
    flag1 = 0
    flag2 = 0

    while True:
        # fill cell
        list0[i][j] = count
        count = count + 1

        # check escape
        if count > n * n:
            break

        # go to next
        prev_pos = (i, j)
        (i, j) = app_marker(i, j, flag1, flag2)

        # check cell
        if (i not in range(n) or j not in range(n)) or list0[i][j] != 0:
            (i, j) = prev_pos
            (flag1, flag2) = app_flag(flag1, flag2)
            (i, j) = app_marker(i, j, flag1, flag2)


# def print_table(slist):
#     for x in slist:
#         print()

# n = 5  # int(input())
# rows, cols = (n, n)
# my_list = [[j for j in range(n)] for i in range(n)]
# print(my_list)

print_snail(4)
