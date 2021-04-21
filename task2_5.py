vowels = 'aоуэыяёеи'
consonants = 'бвгджзхксптфйлмнрхцчшщ'

string = 'Сегодня мы изучаем язык программирования'
string = string.lower()

vow_sum = 0
cons_sum = 0
for char in string:
    if vowels.__contains__(char):
        vow_sum = vow_sum + 1
    elif consonants.__contains__(char):
        cons_sum = cons_sum + 1

vow_perc = vow_sum / len(string) * 100
cons_perc = cons_sum / len(string) * 100

print('Гласных: ', vow_perc, '%')
print('соГласных: ', cons_perc, '%')
