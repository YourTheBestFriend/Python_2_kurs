#-------------------------------------------------------------------------
#5.ВЕТВЛЕНИЯ
#-------------------------------------------------------------------------
# Вариант 6
# Задание 5  2_Способ
#-------------------------------------------------------------------------
from math import*
#
while True:
	try:
		x = float(input('Введите x: '))
		y = sin(x)
		# Через тернарный
		print('Ваше значение y = '+str(y)) if (x >=0 and x <= pi/2) else print('x не соответствует 0 >= x and x <= pi/2')	
		break
	except TypeError:
		print('Error')
		continue
#-------------------------------------------------------------------------