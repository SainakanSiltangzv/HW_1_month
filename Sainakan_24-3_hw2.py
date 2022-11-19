#Основное задание. (до 7 баллов)
day,month = int(input('введите день рождения:')),int(input('введите месяц рождения:'))
if (month==3 and 31>=day>=21) or (month==4 and day<=20):
    print('овен')
elif (month==4 and 30>=day>=21) or (month==5 and day<=21):
    print('телец')
elif (month==5 and 31>=day>=22) or (month==6 and day<=21):
    print('Близнецы')
elif (month==6 and 30>=day>=22) or (month==7 and day<=22):
    print('Рак')
elif (month==7 and 31>=day>=23) or (month==8 and day<=21):
    print('Лев')
elif (month==8 and 31>=day>=22) or (month==9 and day<=23):
    print('Дева')
elif (month==9 and 30>=day>=24) or (month==10 and day<=23):
    print('весы')
elif (month==10 and 31>=day>=24) or (month==11 and day<=22):
    print('скорпион')
elif (month==11 and 30>=day>=23) or (month==12 and day<=22):
    print('стрелец')
elif (month==12 and 31>=day>=23) or (month==1 and day<=20):
    print('козерог')
elif (month==1 and 31>=day>=21) or (month==2 and day<=19):
    print('водолей')
elif (month==2 and 29>=day>=20) or (month==3 and day<=20):
    print('рыбы')
else:
    print('Вы некорректно вввели дату, прошу ввести в следующем формате (день и месяц рождения,через пробел или тире (Например, 24-05)')

# Дополнительное задание (+3 балла)
print('запуск второго задания')
Zodiac = input('Введите день и месяц рождения,через пробел или тире и тп(Например, 24-05):')
day,month = int(Zodiac[:2]),int(Zodiac[3:])
if (month==3 and 31>=day>=21) or (month==4 and day<=20):
    print('овен')
elif (month==4 and 30>=day>=21) or (month==5 and day<=21):
    print('телец')
elif (month==5 and 31>=day>=22) or (month==6 and day<=21):
    print('Близнецы')
elif (month==6 and 30>=day>=22) or (month==7 and day<=22):
    print('Рак')
elif (month==7 and 31>=day>=23) or (month==8 and day<=21):
    print('Лев')
elif (month==8 and 31>=day>=22) or (month==9 and day<=23):
    print('Дева')
elif (month==9 and 30>=day>=24) or (month==10 and day<=23):
    print('весы')
elif (month==10 and 31>=day>=24) or (month==11 and day<=22):
    print('скорпион')
elif (month==11 and 30>=day>=23) or (month==12 and day<=22):
    print('стрелец')
elif (month==12 and 31>=day>=23) or (month==1 and day<=20):
    print('козерог')
elif (month==1 and 31>=day>=21) or (month==2 and day<=19):
    print('водолей')
elif (month==2 and 29>=day>=20) or (month==3 and day<=20):
    print('рыбы')
else:
    print('Вы некорректно вввели дату, прошу ввести в следующем формате (день и месяц рождения,через пробел или тире (Например, 24-05)')

