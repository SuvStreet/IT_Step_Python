from tkinter import *  # импортирование библиотеки tkinter

root = Tk() # создание окна
root.title("Тут отображается название окна.") # заголовок окна

# Метка
lab = Label(root,
            text = "Это метка! \n Из двух строк.", # многострочный текст
            font = "Arial 18") # шрифт текста и его размер

lab.pack() # упаковка параметров метки в lab

root.mainloop() # запуск цикл обработки событий
