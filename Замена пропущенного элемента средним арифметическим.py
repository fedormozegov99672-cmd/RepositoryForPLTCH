numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
for i in range(0, len(numbers)-1):
    if type(numbers[i]) != int:
        numbers[i] = (sum(numbers[:i])+sum(numbers[i+1:]))/len(numbers)
        break
print("Измененный список:", numbers)
