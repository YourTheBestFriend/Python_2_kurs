#-------------------------------------------------------------------------
#16. ПРЕОБРАЗОВАНИЕ МАТРИЦ
#-------------------------------------------------------------------------
# Вариант 6
# Задание 16
#-------------------------------------------------------------------------
# Взял свою функцию из задания 19
from Задание_19 import funk_zapolnenie_massiva
'''
array_1 = []
funk_zapolnenie_massiva(array_1)
print(array_1)
'''
# Если надо для вводо то можно использовать мою функцию, но я для наглядности сам создал массив

# Для теста 
array = [['1','2','3','4'], # Должна перевернуться 
		 ['1','2','3','4'],
		 ['5','6','7','8'], # Должна перевернуться 
		 ['5','6','7','8'], 
		 ['1','2','3','4']] # Должна перевернуться

index = 0

for i in range(len(array)):
	if (index % 2 == 0 or index == 0):
		array[index].reverse()
		index +=1
	else:
		index +=1
		continue

for i in range(len(array)):
	print(array[i])
#-------------------------------------------------------------------------