data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
#1) Создать два пустых списка letters и numbers
letters = []
numbers = list()
#2) Пройтись циклом for по кортежу data_tuple, добавить все строки в список letters, а всё остальное в numbers.
for i in data_tuple:
    #if type(i)==str or type(i)==bool:
        #letters.append(i)
    if isinstance(i,str):
        letters.append(i)
    else:
        numbers.append(i)
# лист копл

'''
Результат
letters ['h', 'C', 'e', 'T', True, 'k', 'e', 'e', 'g'] 
numbers [6.13, 3, 1]
'''

#3) Из списка numbers удалить число 6.13 и переместить True в конец списка letters, затем вставить число 2 между 3 и 1
numbers.remove(6.13)
numbers.insert(1,2)
deleted_True = letters.pop(4) #вырезать
letters.append(deleted_True) #вставить

'''
Результат
letters ['h', 'C', 'e', 'T', 'k', 'e', 'e', 'g', True] 
numbers [3, 2, 1]
'''

#4) Отсортировать numbers, реверсировать letters и изменить пару букв в letters.
numbers.sort()
letters.reverse()
letters[1] = letters[1].upper()
letters[7] = letters[7].lower()

'''
Результат
letters [True, 'G', 'e', 'e', 'k', 'T', 'e', 'c', 'h'] 
numbers [1, 2, 3]
'''

# 5)Измените список numbers в список квадратов своих же чисел
numbers = [i**2 for i in numbers]

'''
Результат
letters [True, 'G', 'e', 'e', 'k', 'T', 'e', 'c', 'h'] 
numbers [1, 4, 9]
'''

# 6) Преобразовать списки numbers и letters в кортежи
numbers = tuple(numbers)
letters = tuple(letters)
print('letters',letters,'\nnumbers',numbers)

'''
В итоге: 
кортеж letters должен выглядеть так:   (True, 'G', 'e', 'e', 'k', 'T', 'e', 'c', 'h')
кортеж numbers должен выглядеть так:   (1, 4, 9)
'''