
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
        print('Выберите один из вариантов.')
        return choice()
    return choice_input


def number_phone():
    num_phone = input('Введте Ваш телефон для регистрации: ')
    phone_n = ''
    for i in num_phone:
        if i.isdigit():
            phone_n += i
    if len(phone_n) < 8:
        print('Повторите ввод, Вы ввели недостаточно цифр!')
        return number_phone()
    elif len(phone_n) >= 9:
        phone_n = '380' + phone_n[-9:]
    return phone_n


def check_phone(phone):
    with open('number_phone.txt') as f:
        for i in f.readlines():
            tmp_num = i.count(phone, 0, 12)
            if tmp_num != 0:
                print('Пользователь с таким номером уже существует')
                return main()
    return


def email_form():
    email_f = input('Введте Ваш емейл: ')
    if len(email_f) < 6 or email_f.count('@') != 1:
        print('Введите емейл правильно')
        return email_form()
    return email_f


def password():
    password_i = input('Введите пароль: ')
    tmp_upper = tmp_lover = tmp_digit = tmp_sam = 0
    if len(password_i) > 7 and password_i.count(' ') == 0:
        for i in password_i:
            if i.isupper():
                tmp_upper = 1
            elif i.islower():
                tmp_lover = 1
            elif i.isdigit():
                tmp_digit = 1
            elif not i.isspace():
                tmp_sam = 1
    if tmp_upper + tmp_lover + tmp_digit + tmp_sam == 4:
        print('Пароль подходит')
    else:
        print('В пароле не должно быть пробелов, минимум одна буква в нижнем регистре, '
              'одна буква в верхнем регистре и одна цыфра и спецсимвол. Введите пароль еще раз.')
        return password()
    password_i2 = input('Введите пароль еще раз для подтверждения: ')
    if password_i != password_i2:
        print('Пароли не савпадают!')
        return password()
    else:
        return password_i


def save_user(*args):
    with open('number_phone.txt', 'a') as f:
        print(*args, file=f)


def main():
    choice_var = choice()
    if choice_var == 1:
        number_phone_var = number_phone()
        check_phone(number_phone_var)
        email_form_var = email_form()
        password_var = password()
        user = f'{number_phone_var} {email_form_var} {password_var}'
        save_user(user)
        print(
            f'\nПоздравляем с успешной регистрацией!\n'
            f'Ваш номер телефона: {number_phone_var}\n'
            f'Ваш email: {email_form_var}\n'
            f'Ваш пароль: {len(password_var) * "*"}\n'
        )
        return main()

    elif choice_var == 2:
        pass


if __name__ == '__main__':
    main()