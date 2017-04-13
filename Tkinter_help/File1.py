from tkinter import *  # импортирование библиотеки tkinter

root = Tk() # создание окна
root.title("Widjets 1") # заголовок окна

# Кнопка
but = Button(root,
             text = 'This is Button', # нименование кнопки
             width = 30, # ширина кнопки
             height = 5, # высота кнопки
             bg = 'orange', # цвет кнопки
             fg = 'blue',# цвет текста
             font = 'Arial 18') # шрифт текста и его размер

but.pack() # упаковка параметров кнопки в but

# Метка
lab = Label(root,
            text = "Это метка! \n Из двух строк.", # многострочный текст
            font = "Arial 18") # шрифт текста и его размер

lab.pack() # упаковка параметров метки в lab

# Однострочное текстовое поле
ent = Entry(root,
            width = 20, # ширина поля отоброжаемых символов
            bd = 10) # толщина края рамок

ent.pack() # упаковка параметров однострочного текстового поля в ent

# Многострочное текстовое поле
tex = Text(root,
           width = 20, # ширина поля отоброжаемых символов
           height = 5, # высота поля
           font = "Verdana 12", # шрифт текста и его размер
           wrap = WORD) # параметр переноса WORD - пернос текста когда он упрётся в width
                                             # NONE - нулевое значение

tex.pack() # упаковка параметров многострочного текстового поля в tex

# Радиокнопки
var = IntVar() # IntVar специальный класс библиотеки для работы с целыми числами
#var.set(1)???
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

# Списки
r = ['Linux', 'Python', 'Tk', 'Tkinter','Igor']
lis = Listbox(root, selectmode=EXTENDED, height=5)
for i in r:
     lis.insert(END,i)
lis.pack()


root.mainloop()
