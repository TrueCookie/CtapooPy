# 2.2

def int_list_input():
    d = input('Введите числа ')
    s = d.split()
    r = [int(x) for x in s]
    return r


def indexes(nums, target):
    count = 0
    index_list = []
    for i in nums:
        if i == int(target):
            index_list.append(count)
        count = count + 1
    return index_list


a = int_list_input()
n = input('Введите число ')
result = indexes(a, n)

if len(result) == 0:
    print('Отсутствует')
else:
    print(result)
