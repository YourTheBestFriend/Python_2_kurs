# alp = 'abcdefghijklmnopqrstuvwxyz'

# формирование словаря кода
def form_dict():
    d = {}
    alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ' + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper()

    # d = alp.split(' ')
    # iter = 0
    # for i in range(0,127):
    #     print(chr(i))
    #     d[iter] = chr(i)
    #     iter = iter +1
    # print(d)
    iter = 0
    for i in range(0,len(alp)):
        d[iter] = alp[iter]
        iter = iter + 1
    # print(d)
    return d
 
# кодируем слова в буквы   
def encode_val(word):
    list_code = []
    lent = len(word)
   
    d = form_dict() # получаем словарь кода
    
    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
               list_code.append(value) 
    return list_code
 
# компаратор 2-х списков
def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0
    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0 
 
    return dic  
 
# finish full encode   
def full_encode(value, key):
 
    dic = comparator(value, key)
    # print('Compare full encode',dic)
  
    lis = []
    d = form_dict()
 
    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go) 
    return lis
 
 
    
##### DECODER
 
# decode to numeric values
def full_decode(value, key):
 
    dic = comparator(value, key)
    
    # print('Deshifre=', dic)
    d = form_dict() # получаем словарь кода
 
    lis =[]
    for v in dic:
        go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
        lis.append(go) 
    return lis
    
 
def decode_val(list_in):
 
    list_code = []
    lent = len(list_in)
 
    d = form_dict() # получаем словарь кода
    
    for i in range(lent):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value]) 
    return list_code
 
if __name__ == "__main__":
 
    word = 'В симметричной криптосистеме секретный ключ передается по защищенному каналу'
    key = 'Справочник'
    
    print('Слово = ', word)
    print('Ключ = ', key)
    
    # print(form_dict())
    # Закодировали буквы в цифры
    key_encoded = encode_val(key)
    value_encoded = encode_val(word)
 
    # print ('Value=',value_encoded)
    # print ('Key=', key_encoded)
 
    # сдвигаем
    shifre = full_encode(value_encoded, key_encoded)
    print('Шифр =', ''.join(decode_val(shifre)))
 
    decoded = full_decode(shifre, key_encoded)
    # print('Decode list=', decoded)
    decode_word_list = decode_val(decoded)
    print('Word =',''.join(decode_word_list))
