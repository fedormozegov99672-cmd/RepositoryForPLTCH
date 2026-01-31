# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, r=","):
    first = set(first.split(r))
    second = set(second.split(r))
    common = first.intersection(second)
    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group,'|'))
