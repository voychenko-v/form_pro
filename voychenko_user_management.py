from pathlib import Path
path = Path(__file__).resolve()
path = path.parent
file_path = path / "number_phone.txt"


def choice():
    print('Главное меню\n'
          '1. Зарегистрировать нового пользователя\n'
          '2. Вывести список новых пользователей\n'
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
    with open(file_path) as f:
        for i in f.readlines():
            tmp_num = i.count(phone, 0, 12)
            if tmp_num != 0:
                print('Пользователь с таким номером уже существует\n')
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
    with open(file_path, 'a') as f:
        print(*args, file=f)


def print_register(phone, email, password_):

    print(
        f'\nПоздравляем с успешной регистрацией!\n'
        f'Ваш номер телефона: {phone}\n'
        f'Ваш email: {email}\n'
        f'Ваш пароль: {len(password_) * "*"}\n'
    )
    return


def num_users():
    list_users = []
    count_user = 0
    with open(file_path, 'r') as f:
        f.seek(0)
        for i in f.readlines():
            list_users.append(i[:-1])
            count_user += 1
        print(f'\nКоличество зарегистрированых пользователей: {count_user}')
    return list_users


def num_list_users(list_user):
    index_user = 1
    str_phone = ''
    for i in list_user:
        i = i.split(' ')
        user_name = i[0]
        str_phone += f'{index_user}. {user_name}\n'
        index_user += 1
    return print(str_phone)


def info_user(list_user):
    chois_num = input('Для отображения детальной информации пользователя, выберите порядковый номер :')
    if chois_num.isdigit():
        chois_num = int(chois_num) - 1
    else:
        return info_user(list_user)
    if chois_num in range(1, len(list_user)):
        info_print = list_user[chois_num].split(' ')
        return print(f'\nНомер телефона: {info_print[0]}\n'
                     f'Емейл: {info_print[1]}\n'
                     f'Пароль: {info_print[2]}\n')
    print(f'\nВыберите число от 1 до {len(list_user)}')
    return info_user(list_user)


def main():
    choice_var = choice()
    if choice_var == 1:
        number_phone_var = number_phone()
        check_phone(number_phone_var)
        email_form_var = email_form()
        password_var = password()
        user = f'{number_phone_var} {email_form_var} {password_var}'
        save_user(user)
        print_register(number_phone_var, email_form_var, password_var)
        return main()

    elif choice_var == 2:
        num_users_var = num_users()
        yes_no = input('Отобразить всех пользователей? (да/нет): \n')
        if yes_no == 'да':
            num_list_users(num_users_var)
            info_user(num_users_var)
        elif yes_no == 'нет':
            return main()
        else:
            print('Нужно ввести "да" или "нет"\n')
    return main()


if __name__ == '__main__':
    main()

