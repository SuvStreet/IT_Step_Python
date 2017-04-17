class Car(object):

    engine_on = False # двигатель, зажигание
    engine_off = False # глушение двигателя
    driving = False # движение
    deceleration = False # торможение
    light_on = False # включение фар
    light_off = False # выключение фар
    door_on = False # двери открыты
    door_off = False # двери закрыты
    sit_down = False # сесть в автомобиль
    handbrake = False # ручной тормоз
    belt = False # ремень безопасности
    
    def __init__(self):
        print('Привествую вас в симуляторе автомобиля.\n')

    # двигатель, зажигание 1
    def engineOnCar(self):
        if not self.engine_on:
            if self.sit_down == True: # мы находимся в авто
                print('Вы завели машину.\n')
                self.engine_on = True
                self.engine_off = False
            else:
                print('Сядъте в автомобиль, что бы получить управление над ним.\n')
        else:
            print('Ваш атомобиль уже заведён.\n')

    # глушение двигателя 2
    def engineOffCar(self):
        if not self.engine_off:
            if self.sit_down == True: # мы находимся в авто
                if self.driving == False: # автомобиль стоит
                    print('Вы заглушили двигатель.\n')
                    self.engine_off = True
                    self.engine_on = False
                else:
                    print('Вы не можите заглушить двигатель, т.к. вы находитесь в движении, остановите автомобиль и заглушите двигатель.\n')
            else:
                print('Сядъте в автомобиль, что бы получить управление над ним.\n')
        else:
            print('Ваш атомобиль не заведён.\n')

    # движение автамобиля 3
    def drivingCar(self):
        if not self.driving:
            if self.sit_down == True: # мы находимся в авто
                if self.engine_on == True: # двигатель запущен
                    if self.light_on == True: # фары включены
                        if self.belt == True: # ремень пристёгнут 
                            if self.handbrake == True: # ручник снят
                                if self.door_off == True: # двери закрыты 
                                    print('Поехалииииииииии... =)\n')
                                    self.driving = True
                                else:
                                    print('Закройте двери, что бы начать движение.\n')
                            else:
                                print('Снимите авто с ручника.\n')
                        else:
                            print('Пристигните ремень.\n')
                    else:
                        print('Включите фары.\n')
                else:
                    print('Завидите для начало ваше авто.\n')
            else:
                print('Сядъте в автомобиль, что бы получить управление над ним.\n') 
        else:
            print('Вы уже в движении.\n')

    # торможение 4
    def decelerationCar(self):
        if not self.deceleration:
            if self.sit_down == True: # мы находимся в авто
                if self.driving == True: # машина находится в движении
                    print('Ваша машина затормозила.\n')
                    self.deceleration = True
                    self.driving = False
                else:
                    print('Вы стоите на месте, начните движение, что бы остановить автомобиль.\n')
            else:
                print('Сядъте в автомобиль, что бы получить управление над ним.\n')
        else:
            print('Вы стоите на месте.\n')

    # открытие дверей 5
    def doorOnCar(self):
        if not self.door_on:
            if self.driving == False: # автомобиль стоит
                print('Вы открыли дверь автомобиля и сели в него.\n')
                self.door_on = True
                self.door_off = False
                self.sit_down = True
            else:
                print('Открытие дверей невозможно, т.к. вы находитесь в движении.\n')
        else:
            print('Двери уже открыты.\n')

    # закрытие дверей 6
    def doorOffCar(self):
        if not self.door_off:
            if self.door_on == True: # открыты двери
                print('Вы закрыли дверь автомобиля.\n')
                self.door_off = True
                self.door_on = False
            else:
                print('Для начало откройте дверь.\n')
        else:
            print('Двери уже закрыты.\n')

    # включить фары 7
    def lightOnCar(self):
        if not self.light_on:
            if self.sit_down == True: # мы находимся в авто
                if self.engine_on == True: # машина заведена
                    print('Вы включили фары.\n')
                    self.light_on = True
                    self.light_off = False
                else:
                    print('Завидите для начало ваше авто.\n')
            else:
                print('Сядъте в автомобиль, что бы получить над ним управление.\n')
        else:
            print('Фары включены.\n')

    # выключить фары 8
    def lightOffCar(self):
        if not self.light_off:
            if self.light_on == True: # фары включены
                if self.sit_down == True: # мы находимся в авто
                    if self.driving == False: # автомобиль стоит
                        print('Вы выключили фары.\n')
                        self.light_off = True
                        self.light_on = False
                    else:
                        print('Вы находитесь в движущимся автомобиле, в ночное время суток, выключить фары нельзя, остановите авто, что бы погасить свет.\n')
                else:
                    print('Сядъте в автомобиль, что бы получить над ним управление.\n')
            else:
                print('Включите сначало фары, чтобы их выключать.\n')
        else:
            print('Фары выключены.\n')

    # ручной тормоз 9
    def handbrakeCar(self):
        if not self.handbrake:
            if self.sit_down == True: # мы находимся в авто
                print('Вы сняли машину с ручника.\n')
                self.handbrake = True
            else:
                print('Сядъте в автомобиль, что бы получить над ним управление.\n')
        else:
            print('Ручник снят.\n')
            
    # ремень безопасности 10
    def beltCar(self):
        if not self.belt:
            if self.sit_down == True: # мы находимся в авто
                print('Вы пристигнули ремень.\n')
                self.belt = True
            else:
                print('Сядъте в автомобиль, что бы получить над ним управление.\n')
        else:
            print('Ремень пристёгнут.\n')

            
# main
import os
car = Car()

choice1 = True
while choice1:
    print('Какое время суток за окном:\n'
          +'1.День\n'
          +'2.Ночь\n\n'
          
          +'0.Выйти из симулятора\n')

    choice1 = int(input('Выш выбр: '))

    os.system('cls')
    car.engine_on# двигатель, зажигание
    car.engine_off = False # глушение двигателя
    car.driving = False # движение
    car.deceleration = False # торможение
    car.light_on = False # включение фар
    car.light_off = False # выключение фар
    car.door_on = False # двери открыты
    car.door_off = False # двери закрыты
    car.sit_down = False # сесть в автомобиль
    car.handbrake = False # ручной тормоз
    car.belt = False # ремень безопасности
    
    choice2 = True
    if choice1 == 1: # День
        
        while choice2:
            print('День.\n')
            print('Функционал вашей машины:\n'
                  +'1.Завести\n'
                  +'2.Заглушить\n'
                  +'3.Поехать\n'
                  +'4.Затормозить\n'
                  +'5.Открыть двери\n'
                  +'6.Закрыть двери\n'
                  +'7.Снять с ручника\n'
                  +'8.Пристигнуть ремень\n\n'
                  
                  +'9.Поменять время суток\n'
                  +'0.Выйти из симулятора\n\n')
            
            choice2 = int(input('Выш выбр: '))

            os.system('cls')
            car.light_on = True
            
            if choice2 == 1: # зажигание
                car.engineOnCar()
                
            elif choice2 == 2: # заглушить
                car.engineOffCar()
                
            elif choice2 == 3: # езда
                car.drivingCar()
                
            elif choice2 == 4: # торможение
                car.decelerationCar()
                
            elif choice2 == 5: # открыть двери
                car.doorOnCar()
                
            elif choice2 == 6: # закрыть двери
                car.doorOffCar()
                
            elif choice2 == 7: # снять с ручника
                car.handbrakeCar()
                
            elif choice2 == 8: # ремень безопасности
                car.beltCar()
                
            elif choice2 == 9: # поменять время суток
                print('Обратите ваше внимание, что при смене времени суток, настройки вашего автомобиля, выставятся по умолчанию.\n')
                input('Нажмите Enter, что бы продолжить.\n')
                os.system('cls')
                choice2 = False
                
            elif choice2 == 0: # выход из программы
                print("Ждёмс, вас вновь ;-).\n")
                choice2 = False
                choice1 = False
           
            else:
                print('Введите корректный номер меню.\n') 

    elif choice1 == 2: # Ночь
        
        while choice2:
            print('Ночь.\n')
            print('Функционал вашей машины:\n'
                  +'1.Завести\n'
                  +'2.Заглушить\n'
                  +'3.Поехать\n'
                  +'4.Затормозить\n'
                  +'5.Открыть двери\n'
                  +'6.Закрыть двери\n'
                  +'7.Включить фары\n'
                  +'8.Выключить фары\n'
                  +'9.Снять с ручника\n'
                  +'10.Пристигнуть ремень\n\n'
                  
                  +'11.Поменять время суток\n'
                  +'0.Выйти из симулятора\n\n')

            choice2 = int(input('Выш выбр: '))

            os.system('cls')
            
            if choice2 == 1: # зажигание
                car.engineOnCar()
                
            elif choice2 == 2: # заглушить
                car.engineOffCar()
                
            elif choice2 == 3: # езда
                car.drivingCar()
                
            elif choice2 == 4: # торможение
                car.decelerationCar()
                
            elif choice2 == 5: # открыть двери
                car.doorOnCar()
                
            elif choice2 == 6: # закрыть двери
                car.doorOffCar()
                
            elif choice2 == 7: # включить фары
                car.lightOnCar()
                
            elif choice2 == 8: # выключить фары
                car.lightOffCar()
                
            elif choice2 == 9: # снять с ручника
                car.handbrakeCar()
                
            elif choice2 == 10: # ремень безопасности
                car.beltCar()
                
            elif choice2 == 11: # поменять время суток
                print('Обратите ваше внимание, что при смене времени суток, настройки вашего автомобиля, выставятся по умолчанию.\n')
                input('Нажмите Enter, что бы продолжить.\n')
                os.system('cls')
                choice2 = False
           
            elif choice2 == 0: # выход из программы
                print("Ждёмс, вас вновь ;-).\n")
                choice2 = False
                choice1 = False
           
            else:
                print('Введите корректный номер меню.\n') 

    elif choice1 == 0: # Выйти
        print("Ждёмс, вас вновь ;-).\n")
        choice1 = False

    else:
        print('Введите корректный номер меню.\n')
        
input('Нажмите Enter, чтобы подтвердить ваш выход.')
