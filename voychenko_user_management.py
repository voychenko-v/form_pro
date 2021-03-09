

def choice():
    print('Главное меню\n'
          '1. Зарегистрировать нового пользователя\n'
          '2. Вывестисписок новых пользователей\n'
          '3. Выход\n')
    num_c = input('Сделайте выбор: ')
    if num_c == '1':
        choice_input = 1
    elif num_c == '2':
        choice_input = 2
    elif num_c == '3':
        print('Выход выполнен')
        return exit()
    else:
        print('Выберите 1 или 2')
        return choice()
    return print(choice_input)


def number_phone():
    num_phone = input('Введте Ваш телефон: ')
    phone_n = ''
    for i in num_phone:
        if i.isdigit():
            phone_n += i
    if len(phone_n) < 8:
        print('Повторите ввод, Вы ввели недостаточно цифр!')
        return number_phone()
    elif len(phone_n) >= 9:
        phone_n = '380' + phone_n[-9:]
        with open('number_phone.txt', 'r+') as f:
            f.seek(0)
            for i in f.readline():
                if i is f.readline():
                    return print('Пользователь с таким номером уже зарегистрирован')
    return phone_n


def email_form():
    email_f = input('Введте Вашу емейл: ')
    if len(email_f) < 6 or email_f.count('@') != 1:
        print('Введите емейл правильно')
        return email_form()
    return email_f


def password():
    password_i = input('Введите пароль: ')
    if len(password_i) > 7 and password_i.count(' ') == 0 and password_i.isupper()\
            and password_i.islower() and password_i.isdigit() is True:
        print('Пароль подходит')
    else:
        print('В пароле не должно быть пробелов, минимум одна буква в нижнем регистре, '
              'одна буква в верхнем регистре и одна цыфра. Введите пароль еще раз.')
        return password()

    password_i2 = input('Введите пароль еще раз для подтверждения: ')
    if password_i != password_i2:
        print('Пароли не савпадают!')
        return password()
    else:
        password_print = len(password_i) * '*'
        return password_print


def reade(*args, **kwargs):
    pass


def main():
    pass


if __name__ == '__main__':
    main()