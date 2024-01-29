from datetime import datetime as dt
def add_record_log(data):
    with open('log.csv', 'a', encoding= 'cp1251') as file:
        time = dt.now().strftime('%H:%M')
        file.write(f'{time}; добавлена запись; {data}\n')

def delete_record_log(data):
    with open('log.csv', 'a', encoding='cp1251') as file:
        time = dt.now().strftime('%H:%M')
        file.write(f'{time}; удалена запись; {data}\n')

def update_record_log(old, new):
    with open('log.csv', 'a', encoding='cp1251') as file:
        time = dt.now().strftime('%H:%M')
        file.write(f'{time}; изменена запись; {old}\n')
        file.write(f'{time}; новая запись; {new}\n')