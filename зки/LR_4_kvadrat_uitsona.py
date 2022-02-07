import random
class Key:
  """
  Класс для генерации и обращение с ключем.
  Сам ключ представлен как две строки с перемешанным алфавитом
  """
  ALPHABET_DEFAULT = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя .!,-1234567890?"
  ROWS_DEFAULT = 7
  COLS_DEFAULT = 7
  def __init__(self,alphabet=ALPHABET_DEFAULT, rows=ROWS_DEFAULT, cols=COLS_DEFAULT):
    """
    Принимает на вход символы алфавита и размер таблицы,
    либо использует алфавит по умолчанию
    """
    self.rows = rows
    self.cols = cols
    self.table=[0]*2
    for i in range(2):
      self.table[i] = list(alphabet)
      random.shuffle(self.table[i])
      self.table[i] = ''.join(self.table[i])

  def __getitem__(self, key):
    """
    Если передали кортеж из двух элементов, 
    то это поиск символа в левой (0) или правой (1) таблице
    Если передали кортеж из трех элементов,
    то это получение символа в таблице по координатам
    """
    if len(key) == 2:
      #table and char
      i = self.table[key[0]].index(key[1])
      return i // self.cols, i % self.cols
    else:
      return self.table[key[0]][key[1]*self.cols+key[2]]

  def __str__(self):
    """
    Для отображения ключа в читабельном виде
    """
    s = ""
    for i in range(self.rows):
      s+=self.table[0][i*self.cols:(i+1)*self.cols]+"\t\t"+self.table[1][i*self.cols:(i+1)*self.cols]+"\n"
    return s
  
def bgrams(l):
  """
  Генератор для разбиения строки на биграммы
  """
  for i in range(0, len(l), 2):
    yield l[i:i + 2]

def crypt(s, key):
  """
  Функция шифровки/дешифровки.
  Пробегаемся по всем биграммам и для каждой биграммы
  находим координаты первого символа в первой таблице,
  второго во второй таблице.
  Далее получаем символы из противоположных вершин прямоугольника
  и добавляем к строке с результатом
  """
  assert len(s) % 2 == 0, "String must divedes by 2"
  r=""
  for bg in bgrams(s):
    (x1, y1), (x2, y2) = key[(0, bg[0])],key[(1, bg[1])]
    r+= key[(0, x2, y1)] + key[(1, x1, y2)]
  return r

#Проверка работоспособности
key = Key()
print(key)
s = crypt("В симметричной криптосистеме секретный ключ передается по защищенному каналу".lower(), key)
print(s)
s = crypt(s, key)
print(s)