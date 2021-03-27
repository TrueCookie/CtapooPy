def pow_even(num):
    if num % 2 == 0:
        return num ** 2
    return num


def list_pow_even(num_list):
    return list(map(pow_even, num_list))


nums = [1, 2, 4, 13, 6]
print(list_pow_even(nums))
