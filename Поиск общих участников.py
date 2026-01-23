# TODO Напишите функцию find_common_participants
def find_common_participants(first, second):
    common = []
    for i in first.split('|'):
        for j in second.split('|'):
            if i == j:
                common.append(i)
    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))
