# Вариант 12
from math import*
# quadrangle - четырехугольник
i = 0
class quadrangle(object):	
	# Если неизвестно
	################################################  
	name = "quadrangle" # Четырехугольник
	# Для показа object 1, object 2 ..
	naimenovanie = "object " # Наименование
	
	# Четыре точки четырезугольника
	point_1 = [0,0]
	point_2 = [0,0]
	point_3 = [0,0]
	point_4 = [0,0]
	
	# По дефолту у четырехугольника 4 стороны
	colvo_storon = 4
	# Периметр и Площадь
	P = 0
	S = 0
	################################################ 
	
	# Для вычисления сторон
	first_side = 0
	second_side = 0
	third_side = 0
	fourth_side = 0

	# Для катетов из треугольников
	# 1
	X_first_side = 0
	Y_first_side = 0
	# 2
	X_second_side = 0
	Y_second_side = 0
	# 3
	X_third_side = 0
	Y_third_side = 0
	#
	X_fourth_side = 0
	Y_fourth_side = 0

	# Конструктор 
	def __init__(self, point_1, point_2, point_3, point_4, x_1, y_1, szhatie_storoni):	
		# Точки
		self.point_1 = point_1
		self.point_2 = point_2	
		self.point_3 = point_3
		self.point_4 = point_4
		
		# Для смены координат вершины
		self.x_1 = x_1
		self.y_1 = y_1

		# Для сжатия стороны
		self.szhatie_storoni = szhatie_storoni		

		# Стороны (катеты) _____________________________________
		
		# 11111
		self.X_first_side = point_2[0] - point_1[0] if point_1[0] > point_2[0] else point_1[0] - point_2[0] # Какая точка больше то от той отнимать(значит она выше)
		self.Y_first_side = point_2[1] - point_1[1]		
		# 22222
		self.X_second_side = point_2[0] - point_3[0]
		self.Y_second_side = point_3[1] - point_2[1] if point_3[1] > point_2[1] else point_2[1] - point_3[1]
		# 33333
		self.X_third_side = point_3[0] - point_4[0] if point_3[0] > point_4[0] else point_4[0] - point_3[0]
		self.Y_third_side = point_3[1] - point_4[1]
		# 44444
		self.X_fourth_side = point_1[0] - point_4[0] 
		self.Y_fourth_side = point_1[1] - point_4[1] if point_1[1] > point_4[1] else point_4[1] - point_1[1]
		
		# Стороны четырехугольника ______________________________
		self.first_side = sqrt(pow(self.X_first_side, 2) + pow(self.Y_first_side, 2))
		self.second_side = sqrt(pow(self.X_second_side, 2) + pow(self.Y_second_side, 2))
		self.third_side = sqrt(pow(self.X_third_side, 2) + pow(self.Y_third_side, 2))
		self.fourth_side = sqrt(pow(self.X_fourth_side, 2) + pow(self.Y_fourth_side, 2))
		# Периметр
		self.P = self.first_side + self.second_side + self.third_side + self.fourth_side

		global i
		i = i + 1

		self.naimenovanie += str(i)

	# Методы Начало ########################################################################
	
	# декоратор
	def decorate(funk):
		def wrappe(self):
			print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@тут сработал декоратор@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
			return funk(self)
		return wrappezs

	# Вычисление Периметра 
	def vichislene_Pirimetra(self):	
		print(f'Периметр = {self.P}')
	
	# Вычисление Площади
	def vichislene_Ploshadi(self):
		self.S = sqrt( self.P/2*((self.P/2-self.first_side) * (self.P/2-self.second_side) * (self.P/2-self.third_side) * (self.P/2-self.fourth_side)))
		print(f'Площадь = {self.S}')

	# Метод print
	@decorate
	def print_info(self):
		print(f'Рисую: {self.name}, {self.naimenovanie},\npoint_1: {self.point_1}\npoint_2 {self.point_2}\npoint_3: {self.point_3}\npoint_4: {self.point_4}')

	# Метод смены координаты вершины (перемещение)
	def point_peremeshenie(self):
		print(f'point_1[0]: {self.point_1[0]}, point_1[1]: {self.point_1[1]}')
		self.point_1[0] = point_1[0] + x_1
		self.point_1[1] = point_1[1] + x_2
		print(f'Сдвиг point_1[0]: {self.point_1[0]} на {self.x_1}, Сдвиг point_1[1]: {self.point_1[1]} на {self.y_1}')

	# Метод сжатия 
	def szatie(self):
		print(f'storona_1: {self.first_side}')
		self.first_side = first_side - szhatie_storoni
		print(f'Сжатие storona_1: {self.first_side} на {self.szhatie_storoni}')

	# Методы Конец ########################################################################


# 111111111111
'''
Точки 4 штуки и у каждой по 2 координаты
'''
object_1 = quadrangle([8,3],[7,8],[5,9],[3,2], 1,1,1)
object_1.print_info()
object_1.vichislene_Pirimetra()
object_1.vichislene_Ploshadi()
# 2
object_2 = quadrangle([3,-5],[6,-7],[2,-8],[1,-7], 1,2,3)
object_2.print_info()
object_2.vichislene_Pirimetra()
object_2.vichislene_Ploshadi()
# 3 
object_3 = quadrangle([-3,-5],[-6,-7],[-2,-8],[-1,-7], 1,2,3)
object_3.print_info()
object_3.vichislene_Pirimetra()
object_3.vichislene_Ploshadi()