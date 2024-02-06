theicon = '|Значок "Extreme demon"|'
theicon1 = 0
theicon2 = 2
apples = '|2 яблока|'
apples1 = 1
apples2 = 2
strongflashlightwithhGERmarking = '|Мощный фонарик с маркировкой "GER"|'
strongflashlightwithhGERmarking1 = 0
strongflashlightwithhGERmarking2 = 2
ajackknife = '|Складной нож|'
ajackknife1 = 0
ajackknife = 2
goldcoins = '|3 золотые монеты|'
goldcoins1 = 1
goldcoins2 = 2
Thend1 = '|Не открыта|'
Thend2 = '|Не открыта|'
Thend3 = '|Не открыта|'
Thend4 = '|Не открыта|'
Thend5 = '|Не открыта|'
a = input('Для начала нажмите любую кнопку')
while a != 'Выход':
    print('МЕНЮ:')
    print('|Играть|')
    print('|Концовки и достижения|')
    print('|Выход|')
    a = input()
    if a == 'Играть' or a == 'играть' or a == '1':
        b = 0
        c = 0
        while b != 'Конец':
            while c != 1:
                print('Вы просыпаитесь не понимая где вы находитесь')
                print('Кругом белый свет и вы не можете ничкго вспомнить')
                print('ЧТО ВЫБЕРИТЕ:')
                print('|1)Осмотреться| >>')
                print('|2)Лечь и спать| >>')
                print('|*Инвентарь*| >>')
                print('|*В главное меню*| >>')
                a = input()
                if a == 'Осмотреться' or a == '1':
                    while c != 1:
                        print('Вы решаите осматреться вдруг что-то найдёте')
                        print('У вас получилось найти какой-то силуэт человека и какие- то строения')
                        print('в остальных направлениях ничего видно не было, одна пустота')
                        print('ЧТО ВЫБЕРИТЕ:')
                        print('|1)Пойти к человеку| >>')
                        print('|2)Пойти в город| >>')
                        print('|3)Пойти в пустоту| >>')
                        print('|4)Лечь и спать| >>')
                        print('|*Инвентарь*| >>')
                        print('|*В главное меню*| >>')
                        a = input()
                        if a == 'Пойти к человеку' or a == '1':
                            while c != 1:
                                print('Вы решили пойти к человеку')
                                print('И замечаите что это стикман')
                                print('Увидев вас он начал тебе махать')
                                print('Подойдя ближе он вам сказал')
                                print('-Здравствуй, ты тут впервые? У меня появился очень серьёзный план')
                                print('Ты ведь не из этого мира нетак ли')
                                print('Я знаю как тебе покинуть этот мир или же ты можешь создать в это мире всё что захочешь')
                                print('Ну так что, согласен?')
                                print('|1)Согласиться| >>')
                                print('|2)Отказаться| >>')
                                print('|3)Послать его н@**й| >>')
                                print('|*Инвентарь*| >>')
                                print('|*В главное меню*| >>')
                        elif a == 'Пойти в пустоту' or a == '3':
                            while C != 1:
                                print('Вы решили двинуться в пустоту вдруг в ней есть что-то что вам')
                                print('вы шли, шли и шли, вы устали ')
                                print('В вашу голову начали проеикать мысли по типу может мне это не нужно, может мне просто остановиться и поспать')
                                print('Ваше действие:')
                                print('|1)Лечь и спать|')
                                print('|2)Идти дальше|')
                                print('|3)Осматреться|')
                                print('|*Инвентарь*|')
                                print('|*В главное меню*|')
                elif a == 'Лечь и спать':
                    print(' ')
                    print('Вы решили ничего не делать, а просто лечь спать')
                    print('Как говорится утро вечера мудренее, но какое утро, какой вечер')
                    print('Вы ложитесь и засыпаите, но незнаите через сколько минут часов но вы просыпаитесь')
                    print('Вы провыпаитесь у себя в постеле. Почему?')
                    print('Тоесть это был всеголишь сон или нет?')
                    if Thend1 == 'Не открыта':
                       print('получена новая концовка')
                       print('Концовка№1 "Сон или нет"')
                       Thend1 = '|(Сон или нет?)|'
                       print(' ')
                       b = 'Конец'
                    else:
                        print(' ')
                        print('Данная концовка уже получена')
                        print('Концовка№1 Сон или нет?""')
                        print(' ')
                        b = 'Конец'
                elif a == 'В главное меню':
                    b = 'Конец'
                    с = 1
                elif a == 'Инвентарь':
                    while a != '':
                        print(' ')
                        print('У вас имеется:')
                        if theicon1 == 0:
                            print(theicon)
                        if strongflashlightwithhGERmarking1 == 0:
                            print(strongflashlightwithhGERmarking)
                        if ajackknife1 == 0:
                            print(ajackknife)
                        print('|*Использовать*|')
                        print('|*Выкинуть*|')
                        print(' ')
                        print('Около вас:')
                        if apples1 == 1:
                            print(apples)
                        if goldcoins1 == 1:
                            print(goldcoins)
                        print('|*Использовать*|')
                        print('|*Взять*|')
                        print(' ')
                        print('|*Назад*|')
                        a = input()
                        if a == 'Использовать' or a == 'использовать':
                            print(' ')
                            if theicon2 == 2:
                                print(theicon)
                            if strongflashlightwithhGERmarking2 == 2:
                                print(strongflashlightwithhGERmarking)
                            if ajackknife2 == 2:
                                print(ajackknife)
                            if apples2 == 2:
                                print(apples)
                            if goldcoins2 == 2:
                                print(goldcoins)
                            print(' ')
                            print('|*Назад*|')
                        elif a == 'Выкинуть' or a == 'выкинуть':
                            if theicon1 == 0:
                                print(theicon)
                            if strongflashlightwithhGERmarking1 == 0:
                                print(strongflashlightwithhGERmarking)
                            if ajackknife1 == 0:
                                print(ajackknife)
                            if apples1 == 0:
                                print(apples)
                            if goldcoins1 == 0:
                                print(apples)
                        elif a == 'Взять' or a == 'взять':
                            print('Выьерите из списка:')
                            print('')
    else:
        if a == 'Концовки и достижения' or a == 'концовки и достижения' or a == '2':
            print('Достижения:')
            print('Концовки:')
            print(Thend1)
            print(Thend2)
            print(Thend3)
            print(Thend4)
            print(Thend5)
            print(' ') 
            print('|Назад|')
            a = input()
            if a == 'Назад' or a == '1':
                continue
