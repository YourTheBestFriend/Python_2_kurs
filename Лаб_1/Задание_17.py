#-------------------------------------------------------------------------
#17. ОБРАБОТКА ПОСЛЕДОВАТЕЛЬНОСТЕЙ СИМВОЛОВ
#-------------------------------------------------------------------------
# Вариант 6
# Задание 17
#-------------------------------------------------------------------------
def my_funk(s):
	index = 0
	# test без заглавных
	list_ = set('bcfghjklmnpqrstvwxyz')
	stroka_2 = ''.join(stroka)
	# 
	for i in stroka_2:
		if i in list_:
			list_.remove(i)
		else:
			list_ = list(list_)
			list_.sort()
	     	# sep – разделяет объекты
	return print(*list_, sep='')

# Просто бахну разделителем по * как по месту разбивки 
stroka = input('Введите строку: ').split('*')
my_funk(stroka)
#-------------------------------------------------------------------------