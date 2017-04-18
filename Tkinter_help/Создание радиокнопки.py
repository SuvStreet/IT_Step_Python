from tkinter import *  # импортирование библиотеки tkinter

root = Tk() # создание окна
root.title("Тут отображается название окна.") # заголовок окна

# Радиокнопки
var = IntVar() # IntVar специальный класс библиотеки для работы с целыми числами
var.set(1) # указывает на активную радиокнопку по умолчанию
rad0 = Radiobutton(root,
                   text = "Первая", # название радиокнопки
                   variable = var, # variable свойство, отвечающее за прикрепление к виджету переменной
                   value = 0).pack() # сразу упаковать , value - в зависимости от того, какой пункт выбран, она меняет своё значение

rad1 = Radiobutton(root, text = "Вторая",
                   variable = var, value = 1)
rad2 = Radiobutton(root, text = "Третья",
                   variable = var, value = 2)

rad1.pack() # упаковываем позже, отдельно
rad2.pack()

root.mainloop() # запуск цикл обработки событий
