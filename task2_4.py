orig_list = str.split(input(), ' ')
index = 0
for cell in orig_list:
    if index % 2 == 1:
        tmp = orig_list[index]
        orig_list[index] = orig_list[index-1]
        orig_list[index-1] = tmp
    index = index + 1

print(orig_list)
