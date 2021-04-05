def str_to_tuple(string):
    string = string.strip()
    string = string.replace(" ", ",")
    return tuple(int(item) for item in string.split(','))


def check_rep(tpl):
    index = 0
    for n in tpl:
        num_rep = tpl[:index].count(n)
        if num_rep >= 1:
            print('YES')
        elif num_rep == 0:
            print('NO')

        index = index + 1


inp = input()
check_rep(str_to_tuple(inp))
