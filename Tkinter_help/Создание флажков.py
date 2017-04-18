from tkinter import *  # импортирование библиотеки tkinter

root = Tk() # создание окна
root.title("Тут отображается название окна.") # заголовок окна

# Флажки
c1 = IntVar()
c2 = IntVar()
che1 = Checkbutton(root,
                   text = "Первый флажок",
                   variable = c1,
                   onvalue = 1, # onvalue, offvalue - свойства, которые присваивают прикреплённой к
                                  # виджету переменной значение, которое зависит от состояния(onvalue - при
                                  # выбранном пункте, offvalue - при невыбранном пункте)
                   offvalue = 0).pack()

che2 = Checkbutton(root,text="Второй флажок",
                   variable=c2, onvalue=1, offvalue=0)
che2.pack()

root.mainloop() # запуск цикл обработки событий
