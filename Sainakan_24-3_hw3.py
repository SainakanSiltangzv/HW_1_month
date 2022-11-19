# Счетчик гласных и согласных букв
glasnye_rus,soglasnye_rus,glasnye_eng,soglasnye_eng ='ауоыиэяюёе','бвгджзйклмнпрстфхцчшщ','aeiouy','bcdfhjklmnpqrstvwxz'

while True:
    word_full = input('введите слово:').lower()
    word = word_full.replace(" ", "")
    GL_r, SGL_r, GL_e, SGL_e = 0, 0, 0, 0
    if word == 'exit' or word == 'выход':
        print('программа завершена!')
        break
    for i in word:
        if i in glasnye_rus:
            GL_r += 1
        elif i in soglasnye_rus:
            SGL_r += 1
        elif i in glasnye_eng:
            GL_e += 1
        elif i in soglasnye_eng:
            SGL_e += 1
    if GL_r>0 or SGL_r>0:
        per_rg,per_rs = round((GL_r/len(word))*100,2),round((SGL_r/len(word))*100,2)
        print(f'Слово: {word_full} \nКоличество букв: {len(word)} \nСогласных букв: {SGL_r} \nГласных букв: {GL_r} \nГласные/Согласные:{per_rg}% / {per_rs}%')
    elif GL_e>0 or SGL_e>0:
        per_eg, per_es = round((GL_e / len(word)) * 100, 2), round((SGL_e / len(word)) * 100, 2)
        print(f'Слово: {word_full} \nКоличество букв: {len(word)} \nСогласных букв: {SGL_e} \nГласных букв: {GL_e} \nГласные/Согласные:{per_eg}% / {per_es}%')

