# Криптосистема была предложена для шифрования телеграфных сообщений

# Для абсолютной криптографической стойкости ключ должен обладать тремя критически важными свойствами:
# 1.	Иметь случайное равномерное распределение:  , где k — ключ, а N — количество бинарных символов в ключе;
# 2.	Совпадать по размеру с заданным открытым текстом;
# 3.	Применяться только один раз.

from random import randint
key=''
keys=''
final=''
# mes = input("Напишите послание, которое хотите зашифровать: ")
mes = 'Допустим это сообщение'.upper()
print('Ваше сообщение: = ' + mes)
for symbol in mes:
    key = randint(0,32); keys += str(key) + "/"
    final += chr((ord(symbol) + key - 17)%33 + ord('А'))

print('Зашифрованное сообщение: ', final.upper())
print ('Ключ шифрования: ',keys)
 
#print('Введите зашифрованное сообщение: ')
#final=input()
#print ('Введите ключ шифрования: ')
#keys = input()
keys =  keys.split('/')
mes = ''

for i, symbol in enumerate(final):
    if keys[i] != '':
        mes += chr((ord(symbol) - int(keys[i])- 17)%33 + ord('А'))

print ('Расшифрованное сообщение : ', mes)