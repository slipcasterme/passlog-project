def check_one(passandlog):    #программа для создания пароля
    if len(passandlog) == 0:
        print('Вы ничего не ввели')
        return False
    if len(passandlog) == 1:
        print('Вы ввели только логин')
        return False
    if len(passandlog) >= 3:
        print('Вы ввели два или более пaроля')
        return False
    if len(passandlog) == 2:
        return True
    
passandlog = input('Введите логин и пароль через пробел: ').split()

if check_one(passandlog):
    print(f'Логин: {passandlog[0]}   Пароль: {passandlog[1]} ')