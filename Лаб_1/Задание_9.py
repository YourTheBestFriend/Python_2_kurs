#-------------------------------------------------------------------------
#9. НАХОЖДЕНИЕ ДЕЛИТЕЛЕЙ ЧИСЛА	
#-------------------------------------------------------------------------
# Вариант 6
# Задание 9
#-------------------------------------------------------------------------

# Для вычисления НОД
def alg_evklid(x, y):
	while x != 0 and y != 0:
		if x > y:
			x %= y
		else:
			y %= x
	otv = x + y 
	return otv

# Ввод
while True:
	try:
		num_1 = int(input('1:'))
		num_2 = int(input('2:'))
		num_3 = int(input('3:'))
		break
	except:
		print('Error')
		continue

# list_ 		
list_ = [num_1, num_2, num_3]

# 1
if (max(list_) == num_1):
	list_[0] = 0
	if (max(list_) == num_2):
		a = alg_evklid(num_1, num_2)
		b = alg_evklid(num_2, num_3)
		if (a > b):
			print(b)
		else:
			print(a)
	else:
		a = alg_evklid(num_1, num_3)
		b = alg_evklid(num_3, num_2)
		if (a > b):
			print(b)
		else:
			print(a)
else:
	# 2	
	if (max(list_) == num_2):
		list_[1] = 0
		if (max(list_) == num_1):
			a = alg_evklid(num_2, num_1)
			b = alg_evklid(num_1, num_3)
			if (a > b):
				print(b)
			else:
				print(a)
		else:
			a = alg_evklid(num_2, num_3)
			b = alg_evklid(num_3, num_1)
			if (a > b):
				print(b)
			else:
				print(a)
	else:
		# 3
		if (max(list_) == num_3):
			list_[2] = 0
			if (max(list_) == num_1):
				a = alg_evklid(num_3, num_1)
				b = alg_evklid(num_1, num_2)
				if (a > b):
					print(b)
				else:
					print(a)
		else:
			a = alg_evklid(num_3, num_2)
			b = alg_evklid(num_2, num_1)
			if (a > b):
				print(b)
			else:
				print(a)

#-------------------------------------------------------------------------