from tkinter import *
from tkinter import messagebox


def registration():
    passandlog = str(passlog_tf.get()).split()
    passandlog = list(passandlog)
    if len(passandlog) == 0:
        messagebox.showinfo('Ошибка', 'Вы ничего не ввели')
    if len(passandlog) == 1:
        messagebox.showinfo('Ошибка', 'Вы ввели только логин')
    if len(passandlog) >= 3:
        messagebox.showinfo('Ошибка', 'Вы ввели два или более паролей')
    if len(passandlog) == 2:
        messagebox.showinfo('Успешно!', f'Логин: {passandlog[0]}   Пароль: {passandlog[1]} ')
        
        

window = Tk()

window.title('Passlog v1')

window.geometry('1080x540')

frame = Frame(
    window,
    padx = 10,
    pady = 10,
)
frame.pack(expand = True)

passlog_lb = Label(
    frame,
    text='Введите логин и пароль через проблем: '
)
passlog_lb.grid(row=3, column=1)

passlog_tf = Entry(
    frame,
)
passlog_tf.grid(row=3, column = 2)

reg_btn = Button(
    frame,
    text='Зарегистрироваться',
    command = registration
)
reg_btn.grid(row = 4, column = 2)

window.mainloop()

# def check_one(passandlog):    #программа для создания пароля
#     if len(passandlog) == 0:
#         print('Вы ничего не ввели')
#         return False
#     if len(passandlog) == 1:
#         print('Вы ввели только логин')
#         return False
#     if len(passandlog) >= 3:
#         print('Вы ввели два или более пaроля')
#         return False
#     if len(passandlog) == 2:
#         return True
    
# passandlog = input('Введите логин и пароль через пробел: ').split()

# if check_one(passandlog):
#     print(f'Логин: {passandlog[0]}   Пароль: {passandlog[1]} ')