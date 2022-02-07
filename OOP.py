import datetime

# Декоратор
def decorator(funk):
	def wrappe(self):
		print('&&&&&&&&&&&&&&&тут сработал декоратор&&&&&&&&&&&&&&&&&&')
		return funk(self)
	return wrappe

now = datetime.datetime.now()
flag_Person = 0
# class
class Person():
	name = "unknown"
	surname = "unknown"
	age = "unknown"
	# Конструктор 
	def __init__(self, name, surname, age):
		self.name = name 
		self.surname = surname
		self.age = age
		# Для счета кол-ва объектов
		global flag_Person
		flag_Person = flag_Person+1
	
	@property
	def temp(self):
		print('Getting')
		return self.name

	@temp.setter
	def temp(self, value):
		print('setting name = ', value)
		self.name = value

	# Метод print
	@decorator
	def display_info(self):
		print(f'name: {self.name}, surname: {self.surname}, age: {self.age}')

	# Метод year_of_birth
	def year_of_birth(self):
		print('Сейчас год:' , now.year, 'В это году -', now.year+1,' - вам будет - ', self.age+1)

	# Деструктор
	def __del__(self):
		print('delete', self.name, self.surname, self.age)
# Создание объекта
p1 = Person("Elon", "Mask", int(49))

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
p1.temp
p1.temp = 'Metvey_2.0'
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

p1.display_info()
p1.year_of_birth()
p2 = Person("Matvey", "Goncharov", int(16))
p2.display_info()
p2.year_of_birth()
#
# pTEST = Person()
# pTEST.display_info()
# pTEST.year_of_birth()
print('Кол-во созданных объектов класса Person: ',flag_Person)

flag_FOR_class_Student = 0
class Student(Person):
	def __init__(self, name, surname, age, avg):
		global flag_FOR_class_Student
		flag_FOR_class_Student = flag_FOR_class_Student+1
		#
		super().__init__(name, surname, age)
		self.avg = avg
	
	# Переназначил метод 
	def display_info():
		print(f'name: {self.name}, surname: {self.surname}, age: {self.age}, avg: {self.avg}')

	# Метод study
	def study(self):
		print(f"{self.name}{self.surname} is study")


##########
Student = Student("Alex", "ger", 15, 8.6)
##########

del Student

flag_FOR_class_Teacher = 0

class Teacher(Person):
	def __init__(self, name, surname, age):
		global flag_FOR_class_Teacher
		flag_FOR_class_Teacher = flag_FOR_class_Teacher+1
		#
		super().__init__(name, surname, age)
	
	# Переназначил метод 
	def display_info():
		print(f'name: {self.name}, surname: {self.surname}, age: {self.age}, avg: {self.avg}')

	# Метод teaching
	def teaching():
		print(f"{self.name}{self.surname} is teaching")

Teacher = Teacher("Anton", "DASD", 21)


print('Кол-во созданных объектов класса Student: ',flag_FOR_class_Student)
print('Кол-во созданных объектов класса Teacher: ',flag_FOR_class_Teacher)