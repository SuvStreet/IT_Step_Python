import random, os

# привествие в игре
print('Привествую в игре двадцать одно.')
print('Правила просты - нужно набрать суммой карт 21.\n')

i = input('Играем на деньги?\n\n"да/нет" = ')
os.system('cls')

# цикл для продолжение игры
game = ''
while game != 'нет':

    if i == 'да':

        ##################################################
        # игра с денегами
        ##################################################

        # интересуемся деньгами игрока
        depozit = int(input("Игрок, сколько у вас деньжат? : "))
        os.system('cls')

        # проверяем положительное ли число
        while depozit > 0:

            # рандомом раздаём по две карты и себе, и банкиру
            mass = [6, 7, 8, 9, 10, 2, 3, 4, 11]
            random.shuffle(mass)
            a = mass.pop(0)
            b = mass.pop(0)
            a += mass.pop(0)
            b += mass.pop(0)

            # банкир ставит ставку
            bank_stav = 100

            # проверяем правильность ставки игрока
            x = False
            while x != True:
                print("Ваш баланс составляет: ", depozit, '$')
                i_stav = int(input('На какую сумму вы рискнёте играть? не более 99$: '))
                if i_stav > depozit:
                    print('\nВоу воу, полегче. Где вы взяли такие деньги, если у вас только', depozit, '$?\n')
                    continue
                if i_stav >= bank_stav:
                    print('\nНу я же попрасил не превышать 99$ Вы первышаете ставку банкира, так делать нельзя!!!\n')
                    continue
                else:
                    x = True
                os.system('cls')

            # продолжение игры
            print('Отлично, когда разобрались с деньгами, начнём игру.\n')
            print('Ваше значение = ', a)

            # цикл работающий только с нами(брать карту следующую или нет)
            karta = ''
            while karta != 'нет':
                karta = input('Взять следующую карту?\n\n"да/нет" = ')
                counter_b = 0 # счётчик приобретёт 1 в случае нашего перебера суммы карт и пропустит цикл с банкиром
                if karta == 'да':
                    os.system('cls')
                    a += mass.pop(0)
                    print('Ваше значение = ', a)
                    if a >= 21:
                        counter_b = 1
                        break

            # цикл работающий только с банкиром(если сумма карт привышает 17,
            # банкир перестаёт брать следующую карту)
            if counter_b == 0:
                while b < 17:
                    b += mass.pop(0)
                    if b > 21:
                        os.system('cls')
                        print('Ваше значение = ', a)
                        print('Значение банкира = ', b)
                        print('\nВы победили! Ура!')
                        depozit += i_stav
                        break

            else:
                print('Значение банкира = ', b)
                print('\nПобедил банкир')
                depozit -= i_stav

            # условия выполняется, если сумма карт не превышает 21, как у банкира, так и у нас
            if a <= 21:
                if b <= 21:

                    if b > a:
                        os.system('cls')
                        print('Ваше значение = ', a)
                        print('Значение банкира = ', b)
                        print('\nПобедил банкир')
                        depozit -= i_stav

                    elif a > b:
                        os.system('cls')
                        print('Ваше значение = ', a)
                        print('Значение банкира = ', b)
                        print('\nВы победили! Ура!')
                        depozit += i_stav

                    elif a == 21:
                        os.system('cls')
                        print('Ваше значение = ', a)
                        print('Значение банкира = ', b)
                        print('\nВы победили! Ура!')
                        depozit += i_stav

                    elif b == 21:
                        os.system('cls')
                        print('Ваше значение = ', a)
                        print('Значение банкира = ', b)
                        print('\nПобедил банкир')
                        depozit -= i_stav

                    else:
                        os.system('cls')
                        print('Ваше значение = ', a)
                        print('Значение банкира = ', b)
                        print('\nПобедила дружба')

            print("\nВаш баланс составляет: ", depozit, '$')

            # проверяем есть ли деньги у игрока, если закончились выходим из игры
            if depozit <= 0:
                print('\nК сожелению у вас закончились деньги\n')
                game = "нет"
                break

            # когда закончилась игра спрашиваем желание продолжение играть
            game = input('\nПродолжить?\n\n"да/нет" = ')
            os.system('cls')
            if game == 'нет':
                os.system('cls')
                break
                
    ##################################################
    # игра без денег
    ##################################################

    if i == 'нет':
        # рандомом раздаём по две карты и себе, и банкиру
        mass = [6, 7, 8, 9, 10, 2, 3, 4, 11]
        random.shuffle(mass)
        a = mass.pop(0)
        b = mass.pop(0)
        a += mass.pop(0)
        print('Ваше значение = ', a)
        b += mass.pop(0)

        # цикл работающий только с нами(брать карту следующую или нет)
        karta = ''
        while karta != 'нет':
            karta = input('Взять следующую карту?\n\n"да/нет" = ')
            counter_b = 0 # счётчик приобретёт 1 в случае нашего перебера суммы карт и пропустит цикл с банкиром
            if karta == 'да':
                os.system('cls')
                a += mass.pop(0)
                print('Ваше значение = ', a)
                if a >= 21:
                    counter_b = 1
                    break

        # цикл работающий только с банкиром(если сумма карт привышает 18,
        # банкир перестаёт брать следующую карту)
        if counter_b == 0:
            while b < 17:
                b += mass.pop(0)
                if b > 21:
                    os.system('cls')
                    print('Ваше значение = ', a)
                    print('Значение банкира = ', b)
                    print('\nВы победили! Ура!')
                    break

        else:
            print('Значение банкира = ', b)
            print('\nПобедил банкир')

        # условия выполняется, если сумма карт не превышает 21, как у банкира, так и у нас
        if a <= 21:
            if b <= 21:

                if b > a:
                    os.system('cls')
                    print('Ваше значение = ', a)
                    print('Значение банкира = ', b)
                    print('\nПобедил банкир')

                elif a > b:
                    os.system('cls')
                    print('Ваше значение = ', a)
                    print('Значение банкира = ', b)
                    print('\nВы победили! Ура!')

                elif a == 21:
                    os.system('cls')
                    print('Ваше значение = ', a)
                    print('Значение банкира = ', b)
                    print('\nВы победили! Ура!')

                elif b == 21:
                    os.system('cls')
                    print('Ваше значение = ', a)
                    print('Значение банкира = ', b)
                    print('\nПобедил банкир')

                else:
                    os.system('cls')
                    print('Ваше значение = ', a)
                    print('Значение банкира = ', b)
                    print('\nПобедила дружба')

        # когда закончилась игра спрашиваем желание продолжение играть
        game = input('\nПродолжить?\n\n"да/нет" = ')
        os.system('cls')

print('Ждёмс вас вновь =D\n')
input('Нажмите Enter, что бы выйти...')
