data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

# 1) Создать два пустых списка designations и codes
designations = list()
codes = []
# 2) Пройтись циклом for по кортежу data, добавить наименования компаний в designations и коды в codes
for i in data:
    if i.isdigit():
        codes.append(i)
    else:
        designations.append(i)

''' 
['0705', '0550', '0770', '0510', '0543'] ['O!', 'Megacom', 'Beeline', 'Katel', 'Fonex']
'''
# 3) Создать словарь operators на основе списков designations и codes c помощью цикла while, где ключами будут названия компаний а значениями коды содержащиеся в множестве (set)!

operators = dict()
while True:
    A = designations.pop()
    B = codes.pop()
    operators[A] = {B}
    if len(codes)<1:
        break
''''
так и не поняла почему так не сработала???
while len(codes) == 0:
    A = designations.pop()
    B = codes.pop()
    operators[A].append(B)
'''
# создать множество с кодами
set1 = ('0700', '0500', '0999', '0555','0222','0777')
set0 = ('0700', '0500')
setB = ('0222','0777')
setM = ('0999', '0555')

# 4) Удалить нефункционирующие операторы из словаря operators. (Katel, Fonex)
del operators ['Katel']
del operators ['Fonex']

#5)Добавить/Обновить к уже существующим номерам (Ошке, Меге и Билайну) пару кодов содержащихся в множестве. Добавить, а не просто переписать вручную в сэт.

operators['O!'].update(set0)
operators['Megacom'].update(setM)
operators['Beeline'].update(setB)

# 6) В итоге вывести на экран наименования операторов и соответствующие номера в таком виде (в паре ключ-значение):
for i in operators:
    print(f'{i} : {operators[i]}')
