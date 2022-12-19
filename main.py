from tkinter import *
from random import choice
#формируем окно
root = Tk()
root.geometry('300x300')
root.resizable(False,False)
root.title(f'Быки и коровы')

#создаём функцию генерации числа для игры
def generation():
    spisok=list(range(0,10)) #создаём список цифр от 0 до 9
    generation_str = '' #создаем пустую строку
    for i in range(0,4): #проходим 4 раза циклом
        a = choice(spisok) #при помощи функции choice из библиотеки random выбираем рандомное число из списка с цифрами
        spisok.remove(a) #удаляем выбранное рандомное число из списка
        generation_str +=str(a) #записываем это число как букву в пустую строку
    return generation_str #после выполнения функции возвращаем сгенерированное число в виде строки

number = generation()  #вызываем функцию и записываем ее результат в переменную number
print(number)
#создаём область главного экрана в которой будет поле ввода и надписи Input:, Попытка, введённое число, результат и кнопка Ок
frame_const = Frame(root, width=300, height=100)
frame_const.place(x='0', y='0')


input_word = Label(frame_const,text=f'Input:')
input_word.place(x=90,y=60,anchor='center')

popytka_word = Label(frame_const,text=f'Попытка')
popytka_word.place(x=60,y=90,anchor='center')

vvod_word = Label(frame_const,text=f'Введённое число')
vvod_word.place(x=150,y=90,anchor='center')

result_word = Label(frame_const,text=f'Результат')
result_word.place(x=240,y=90,anchor='center')

input_enter = Entry(frame_const)
input_enter['width']=10  #ширина видимых символов в поле ввода
input_enter.place(x=150,y=60,anchor='center')


#создаём фрейм в котором будут выводится вводимые числа, число попыток и колличество быков и cow
frame1 = Frame(root, width=300, height=160)
frame1.place(x='0', y='100')


result_game = Label(root,text='')


#задаем начальную позицию по y для вывода попыток и начальное колличество попыток
popytka = 0
position = 10
#задаем функцию которая будет работать при нажатии на кнопку Ок
def button_ok_comand():
    global position,popytka  #делаем переменные глобальными
    chislo=input_enter.get() #берем значения из поля ввода и заносим в переменную chislo
    input_enter.delete(0,END)  #стираем цифры из поля ввода на экране
    popytka += 1   #прибавляем попытку
    byk=0   #вводим колличество быков изначальное
    cow = 0 # и коров
    for i in list(range(0,4)):  #проходим циклом по списку из цифр от 0 до 3
        if chislo[i]==number[i]:  #если число из набора цифр из поля ввода и из сгенерированных совпадают и находятся на одной позиции
            byk+=1 #то мы колличество быков увеличиваем на 1
        elif chislo[i]!=number[i] and chislo[i] in number: #если число из набора цифр из поля ввода и из сгенерированных не совпадают, число из набора цифр из поля ввода есть в списке из сгенерированных
            cow +=1  #то мы колличество коров увеличиваем на 1
    result = f'🐂{byk}🐄{cow}' #в переменную result записываем колличество быков и коров
    #выводим попытки, введенное число, колличество быков и коров
    pop_word = Label(frame1, text=f'{popytka}')
    pop_word.place(x=50, y=position,anchor='center')
    chi_word = Label(frame1, text=f'{chislo}')
    chi_word.place(x=140, y=position,anchor='center')
    res_word = Label(frame1, text=f'{result}')
    res_word.place(x=220, y=position,anchor='center')
    position +=30 #прибавляем к позиции 30
    if popytka == 6: #если колличество попыток равно 6, то выводится сообщение о проигрыше и скрываются два фрейма
        result_game['text'] = 'Вы проиграли'
        result_game.place(relx=0.5,rely=0.3,anchor='center')
        frame1.place_forget()
        frame_const.place_forget()
    elif byk == 4:  #если колличество быков будет равно 4, то выводится сообщение о победе и скрываются два фрейма
        result_game['text'] = 'Вы победили'
        result_game.place(relx=0.5, rely=0.3, anchor='center')
        frame1.destroy()
        frame_const.place_forget()
#функция при нажатии на кнопку начать игру
def button_new_comand():
    global number,popytka,position,frame1
    #генерируем новое число, ставим число попыток 0 и позицию 10
    number = generation()
    popytka = 0
    position = 10
    frame_const.place(x='0', y='0') #покажем на экране область с input, кнопкой Ок и т.д.
    frame1 = Frame(root, width=300, height=160) #а фрейм где были попытки перезапишем, чтобы стереть все что в нем было
    frame1.place(x='0', y='100')
    result_game.place_forget()  #скроем результат игры
def button_exit_comand():
    exit()
#записываем что при нажатии левой кнопкой мыши по такой то кнопке, будет вызывать такую то функцию
button_ok = Button(frame_const,text='Ok',command=button_ok_comand)
button_ok.place(x = 210,y=60,anchor='center')

button_new = Button(root,text='Новая игра',command=button_new_comand)
button_new.place(relx = 0.3,rely=0.9,anchor='center')

button_exit = Button(root,text='Выйти',command=button_exit_comand)
button_exit.place(relx = 0.7,rely=0.9,anchor='center')

root.mainloop()