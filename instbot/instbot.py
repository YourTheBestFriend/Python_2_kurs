from instapy import InstaPy
#import time
from selenium import webdriver

# ник
insta_username = ''
# пароль
insta_password = ''


gg = 1
while gg == 1:
	try:
		global number
		number = int(input('Как найти пользователя |\n1 - по нику\n2 - по ссылке\nВвод $$ -: '))
		gg+=1
	except():
		print('Error | Так не прокатит')

# Чекнуть другого пользователя
if number == 1:
	user_w_inst = input('Введите ник пользователя к которому хотите перейти: ')
if number == 2:
	user_w_inst = input('Введите ссылку пользователя к которому хотите перейти: ')


# webdriver
driver = webdriver.Chrome('C://#WORK//python//instbot//chromedriver.exe')  
# ссылка
link_inst = 'https://www.instagram.com'
# переход по ссылке
driver.get(link_inst)

# При возникновении ошибок
i = 1
while (i == 1):
	try:
		# Ввод ника
		driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("") # 
		driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("") # 
		# Вход click()
		driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click() 
		# Все сработало
		i+=1
	# Error 1.0
	except:
		print('Error 1.0')



# Для ошибок при переходе по нику
if number == 1: 
	# При возникновении ошибок 2
	i2 = 1
	while (i2 == 1):
		try:
			# Страница другого пользователя
			driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(user_w_inst)  
			i2+=1
		# Error 2.0
		except:
			print('Error 2.0')
	i3 = 2
	while (i3 == 2):
		try:
			driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div/div[2]/div/span').click() 
			i3+=1
		# Error 2.0
		except:
			print('Error 3.0')

# Для ошибок при переходе по ссылке
if number == 2:
	i2 = 1
	while (i2 == 1):
		try:
			# Страница другого пользователя
			driver.find_element_by_xpath('').send_keys(user_w_inst)  
			i2+=1
		# Error 2.0
		except:
			print('Error 2.0')
	i3 = 2
	while (i3 == 2):
		try:
			driver.find_element_by_xpath('').click() 
			i3+=1
		# Error 2.0
		except:
			print('Error 4.0')

#driver.quit()

#session = InstaPy(username=insta_username,password=insta_password,geckodriver_path=r'C://#WORK//python//instbot//chromedriver.exe')
#session.login()


