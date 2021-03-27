def app_flag(flag1, flag2):
    if not flag1 and not flag2:  # 00
        flag1 = 0
        flag2 = 1
    elif not flag1 and flag2:  # 01
        flag1 = 1
        flag2 = 0
    elif flag1 and not flag2:  # 10
        flag1 = 1
        flag2 = 1
    elif flag1 and flag2:  # 11
        flag1 = 0
        flag2 = 0
    return flag1, flag2


def app_marker(i, j, flag1, flag2):  # переход к след ячейке
    if not flag1 and not flag2:  # 00
        j = j + 1
    elif not flag1 and flag2:  # 01
        i = i + 1
    elif flag1 and not flag2:  # 10
        j = j - 1
    elif flag1 and flag2:  # 11
        i = i - 1
    return i, j


def create_snail(n):
    list0 = [[0 for j in range(n)] for i in range(n)]
    i = 0
    j = 0
    count = 1
    flag1 = 0
    flag2 = 0

    while True:
        # заполним ячейку
        list0[i][j] = count
        count = count + 1

        # условие выхода
        if count > n * n:
            break

        # переход к след ячейке
        prev_pos = (i, j)  # запоминаем позицию
        (i, j) = app_marker(i, j, flag1, flag2)

        # проверяем условия поворота
        if (i not in range(n) or j not in range(n)) or list0[i][j] != 0:
            (i, j) = prev_pos
            (flag1, flag2) = app_flag(flag1, flag2)
            (i, j) = app_marker(i, j, flag1, flag2)

    return list0


def print_table(dlist):
    for line in dlist:
        for cell in line:
            fixed = "{0: >5}".format(cell.__str__())
            print(fixed, end='')
        print('\n')


n = int(input())
snail_list = create_snail(n)
print_table(snail_list)
