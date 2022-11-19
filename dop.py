'''
Написать функцию “Ближайшее Число”.
Функция должна принимать два параметра:
1) список или кортеж - состоящий из целых или дробных чисел (обязательный параметр)
2) целое или дробное число (параметр по умолчанию)
Функция должна вернуть число из последовательности, которое ближе всего к указанному.
'''

def sort_of_list(lst,number):
    list_of_numbers = []
    for i in lst:
        razn_num = i - number
        list_of_numbers.append(abs(razn_num))
        index_of_number = list_of_numbers.index(min(list_of_numbers)) #это и есть минимальное значение
    return print(lst[index_of_number])

sort_of_list([1,5,9,20,8888,45,62,39,2368,1100,10], 89)

