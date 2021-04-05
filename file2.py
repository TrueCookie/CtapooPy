def fract_sum(num):
    num_str = str(num)
    num_sum = 0

    dot_index = num_str.find('.')
    fract_part = num_str[dot_index+1:]

    for i in fract_part:
        num_sum = num_sum + int(i)
    return num_sum


print(fract_sum(input()))
