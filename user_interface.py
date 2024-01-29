
def menu():
    print('Перед Вами меню, выберите действие:\n\
    1 - Поиск информации в справочнике\n\
    2 - Добавить запись\n\
    3 - Удалить запись\n\
    4 - Изменить запись')
    menu_id = int(input(': '))
    return menu_id

def search_menu():
    print('По каким параметрам производить поиск?:\n\
        1 - Имя\n\
        2 - Фамилия\n\
        3 - Номер телефона\n\
        4 - Номер записи в справочнике\n\
        0 - Вернуться в главное меню')
    menu_id = int(input(': '))
    return menu_id

def search_menu_end():
    print('Что желаете сделать дальше?: \n\
        1 - Редактировать запись \n\
        2 - Удалить запись \n\
        3 - Продолжить поиск\n\
        0 - Возврат в основное меню')
    menu_id = int(input(': '))
    return menu_id

def add_record_view():
    print('Введите параметры для записи: ')

def add_record_sucsess():
    print('Запись успешно добавлена!')

def add_record_menu_end():
    print('Что сделать дальше?: \n\
        1 - Добавить еще одну запись\n\
        0 - Вернуться в основное меню')
    menu_id = int(input(': '))
    return menu_id

def delete_menu():
    print('Меню удаления записи:\n\
        1 - Ввести номер записи\n\
        2 - Произвести поиск записи\n\
        0 - Вернуться в главное меню')
    res = int(input(': '))
    return res

def delete_succses():
    print('Запись успешно удалена!')

def delete_record_menu():
    print('Введите номер записи для удаления: ')
    res = input(': ')
    return res

def delete_menu_end():
    print('Что желаете сделать дальше?:\n\
        1 - Удалить еще одну запись\n\
        0 - Вернуться в главное меню ')
    res = int(input(': '))
    return res

def update_menu():
    print('Меню редактирования записи: \n\
        1 - Ввести номер записи для редактирования \n\
        2 - Произвести поиск записи\n\
        0 - Возврат в основное меню')
    res = int(input(': '))
    return res

def update_record_menu():
    print('Введите номер записи для редактирования: ')
    res = input(': ')
    return res

def update_record_par_menu(data):
    print('Вы редактируете следующую запись: ')
    user_record_view(data)
    print('Что Вы хотите поменять?: \n\
    1 - Имя\n\
    2 - Фамилию\n\
    3 - Телефон\n\
    4 - Комментарий\n\
    0 - Вернуться в основное меню')
    res = int(input(': '))
    return res

def update_sucsess():
    print('Запись успешно изменена!')

def update_menu_end():
    print('Что Вы хотите сделать дальше?: \n\
    1 - Редактировать еще одну запись\n\
    0 - Возврат в главное меню')
    res = int(input(': '))
    return res

def name_input():
    res = input('Введите имя: ')
    return res

def second_name_input():
    res = input('Введите фамилию: ')
    return res

def phone_number_input():
    res = input('Введите номер телефона: ')
    return res

def position_input():
    res = input('Введите номер записи в справочнике: ')
    return res

def comment_input():
    res = input('Введите комментарий: ')
    return res



def user_record_view(list):
    if list == []:
        print('Записи с этими параметрами не найдено!')
    else:
        for x in list:
            print(*x, sep ='|')

def menu_input_error():
    print('Неправильный ввод! Повторите: ')