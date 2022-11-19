start = 0
finish = 100
middle = 50
count = 0

with open('results.txt', 'w', encoding='UTF-8') as file:
    while True:
        print(f"Загаданное вами число равно {middle}?")
        file.write(f'{middle},')
        answer = input()
        count += 1
        if answer.lower() == 'больше':
            start = middle
            middle = (start + finish) // 2
        elif answer.lower() == 'меньше':
            finish = middle
            middle = (start + finish) // 2
        elif answer.lower() == 'да':
            file.write(f"\nКоличество попыток: {count}")
            file.write(f"\nЗагаданное число: {middle}")
            break
        else:
            print('Неправильный ввод. Введите: да,больше или меньше')
