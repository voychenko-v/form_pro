User management - курсовой проект на Python (базовый курс)

        Основные возможности программы:
            - регистрация пользователей
            - просмотр учетных записей
            - хранение базы пользователей в течении сеанса
            ** хранение базы пользователей в файле
            ** сброс пароля пользователей
            ** удаление пользователей

        При запуске программы попадаем в "Главное меню":
            1. Зарегистрировать нового пользователя
            2. Просмотреть список пользователей

        При выборе пункта 1.
            - форма регистрации, аналогичная из hw5/reg_form.py, а именно:
                + ввод номера телефона
                + ввод email адреса
                + ввод и подтверждение пароля
            - номер телефона - уникальный (нельзя зарегистрировать двух пользователей с одинаковым номером телефона)
            - после успешной регистрации выводятся данные о пользователе и попадаем в Главное меню
            - данные о пользователе сохраняются:
                + в переменной
                + для хранения пользователей можно использовать любую структуру данных
                * использовать список словарей либо список объектов класса
                ** сохранять данные в файл (при перезапуске программы данные не теряются)

        При выборе пункта 2.
            - выводится количество зарегистрированных пользователей и
                задается вопрос: "Отобразить всех пользователей? (да/нет)"

                нет - попадаем в Главное меню
                да - переходим к следующему пункту

            - на экран выводится пронумерованный список пользователей (только номера телефонов)
  
