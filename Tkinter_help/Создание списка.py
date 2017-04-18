from tkinter import * # импортирование библиотеки tkinter

root = Tk() # создание окна
root.title("Моё окно.") # заголовок окна

# списки
listbox1 = Listbox(root, height = 5, width = 15, selectmode = EXTENDED) # EXTENDED = позволяет пользователю выбрать любое количество элементов из списка
listbox2 = Listbox(root, height = 5, width = 15, selectmode = SINGLE) # SINGLE = позволяет пользователю выбрать только один элемент списка
list1 = ["Москва", "Санкт-Петербург", "Саратов", "Омск"]
list2 = ["Канберра", "Сидней", "Мельбурн", "Аделаида"]
for i in list1:
    listbox1.insert(END, i)
for i in list2:
    listbox2.insert(END, i)
listbox1.pack()
listbox2.pack()

root.mainloop()
