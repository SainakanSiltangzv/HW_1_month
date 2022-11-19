''''
Написать функцию, которая возвращает первое слово из полученного предложения.
В качестве параметра по умолчанию указать строку “Hello World”
Функция должна Вернуть False, если переданный аргумент не является строкой.
Если в указанном предложении только одно слово, то вернуть это слово.

'''

def first_word(sentence):
    if type(sentence) != str:
        return False
    else:
        return sentence.split()[0]
print(first_word("Hello World"))
#print(first_word(44444)) #вернет False если задать тип данных кроме str

'''
Написать функцию, которая принимает неограниченное количество чисел и возвращает их среднее арифметическое.
Среднее арифметическое должно быть в виде целого числа.
Использовать звёздочку для обозначения последовательности аргументов.
'''
def average_mean(*args):
    print('Средняя арифметическая составлет: ',end="")
    return int(sum(args)/len(args))
print(average_mean(5,63,4,1,8,9,7,63,24,27))

'''
Написать функцию, проверяющую надежность пароля.
Возвращать True если пароль содержит не менее 6 символов, состоящих из цифр и букв, в противном случае вернуть False
'''
def reliable_password(password_):
    if len(password_)>=6 and (not password_.isdigit()) and (not password_.isalpha()):
        return True
    else:
        return False
print(reliable_password(input('Введите пароль: ')))

