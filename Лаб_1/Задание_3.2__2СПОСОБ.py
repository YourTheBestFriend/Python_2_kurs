#-------------------------------------------------------------------------
#3. ЛОГИЧЕСКИЕ ВЫРАЖЕНИЯ
#-------------------------------------------------------------------------
# Вариант 6
# Задание 3.2
#-------------------------------------------------------------------------
# x1, x2, x3, x4
# x1 < x2 > x3 < x4

# 2 Способ
##################
# Для обнуления наибольшего
def zero_for_list(x1, x2, x3, x4):
	if (max(list_) == x1):
		list_[0] = 0
	else:
		if (max(list_) == x2):
			list_[1] = 0
		else:		
			if (max(list_) == x3):
				list_[2] = 0
			else:
				if (max(list_) == x4):
					list_[3] = 0
				else:
					pass	

# Для значений
x2_help = 0
x4_help = 0
x3_help = 0
x1_help = 0

# 1. x2
# 2. x4
# 3. x3
# 4. x1

x1 = int(input('x1: '))
x2 = int(input('x2: '))
x3 = int(input('x3: '))
x4 = int(input('x4: '))

list = [x1, x2, x3, x4]

# x2 - Самое большое 
x2_help =  max(list_)

# x1 - Самое маленькое
x1_help =  min(list_)

# обнуляю x2 в списке, для дальнейшего сравнения 
zero_for_list(x1, x2, x3, x4)

# x4  / больше x3 и x1
x4_help = max(list_)

# обнуляю x4 в списке, для дальнейшего сравнения 
zero_for_list(x1, x2, x3, x4)

# x3 / больше x1 
x3_help = max(list_)

# Пересохраняю обратно
x2 = x2_help
x4 = x4_help
x3 = x3_help 
x1 = x1_help

print(x1, x2, x3, x4)
print(x1 < x2 > x3 < x4)
##################
#-------------------------------------------------------------------------