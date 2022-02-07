#-------------------------------------------------------------------------
#19. ФУНКЦИИ
#-------------------------------------------------------------------------
# Вариант 6
# Задание 19.1, 19.2, 19.3
#-------------------------------------------------------------------------
'''
19.1
Оформлено в задании 1 

19.3
Оформлено в задании 17, 18


19.2
Оформлено в задании 12, 13, 14
и часть тут по - (Заполнение матриц)
функция для заполнения матрицы случайными числами, ввода с
клавиатуры, вывода на экран.
'''

# 19.2
# Я сначало хотел сделать на вход значения m x n (Столбцы и строки), но потом просто передал массив и там далей довал выбор
# Я предворительно рандом ввел в диапазоне от 0 до 100
import random
def funk_zapolnenie_massiva(array):
	while True:
		vibor = input('1.Рандомно заполнить массив\n2.Вручную заполнить масиив\nВвод: ')
		razm = input('3.Статический массив\n4.Динамический\nВвод: ')
		raz = int(input('Введите кол-во столбцов:'))
		# Если динамический 
		if (razm == '4'):
			raz_2 = int(input('Введите кол-во строк:'))
		else: 
			pass
		# По ветке рандома
		if (vibor == '1'):	
			# Статический
			if (razm == '3'):
				for i in range(raz):
					num = random.randrange(0, 101, 1)
					array.append(num)
				return array
			else:
				# Динамический
				if (razm == '4'):
					for i in range(raz):
						array.append([])
						for j in range(raz_2):	
							num = random.randrange(0, 101, 1)
							array[i].append(num) 					
					return array
		else:
			# По ветки ручной
			if (vibor == '2'):
				# Статический
				if (razm == '3'):
					for i in range(raz):
						num = input('array['+str(i) +']: ')
						array.append(num)
					return array
				else:
					# Динамический
					if (razm == '4'):
						for i in range(raz):
							array.append([])
							for j in range(raz_2):	
								num = input('array['+str(i) +']'+'['+str(j)+']: ')
								array[i].append(num) 						
						return array
			else:
				print('Error')
				continue

# Раскоментить для теста 
''' 
array = []
funk_zapolnenie_massiva(array)

for i in len(array):
	print(array[i])
'''
#-------------------------------------------------------------------------