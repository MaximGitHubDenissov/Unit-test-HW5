import user_interface as ui
import operations as oper
import logger as log

def main_menu_button():
    sel_menu = ui.menu()
    if sel_menu == 1:
        search_menu_button()
    if sel_menu == 2:
        add_record_button()
    if sel_menu == 3:
        delete_menu_button()
    if sel_menu == 4:
        update_menu_button()
    

def search_menu_button():
    menu_id = ui.search_menu()
    if menu_id == 1:
        ui.user_record_view(oper.search_record(1, ui.name_input()))
        search_menu_end_button()
    if menu_id == 2:
        ui.user_record_view(oper.search_record(2, ui.second_name_input()))
        search_menu_end_button()
    if menu_id == 3:
        ui.user_record_view(oper.search_record(3, ui.phone_number_input()))
        search_menu_end_button()
    if menu_id == 4:
        ui.user_record_view(oper.search_record(0, ui.position_input()))
        search_menu_end_button()
    if menu_id == 0:
        main_menu_button()
    else:
        search_menu_button()
    

def search_menu_end_button():
    menu_id = ui.search_menu_end()
    if menu_id == 1:
        update_menu_button()
    if menu_id == 2:
        delete_menu_button()
    if menu_id == 3:
        search_menu_button()
    if menu_id == 0:
        main_menu_button()
    

def add_record_button():
    ui.add_record_view()
    name = ui.name_input()
    second_name = ui.second_name_input()
    phone_number = ui.phone_number_input()
    comment = ui.comment_input()
    oper.add_record(name, second_name, phone_number, comment)
    data = ';'.join(oper.enumerate_file())
    log.add_record_log(data)
    ui.add_record_sucsess()
    add_record_menu_end_button()

def add_record_menu_end_button():
    menu_id = ui.add_record_menu_end()
    if menu_id == 1:
        add_record_button()
    if menu_id == 0:
        main_menu_button()
    

def delete_menu_button():
    menu_id = ui.delete_menu()
    if menu_id == 1:
        num = ui.delete_record_menu()
        record = oper.search_record(0, num)
        data = ';'.join(record[0])
        ui.user_record_view(record)
        if record == []:
            delete_menu_button()
        else:
            oper.delete_record(int(num))
            log.delete_record_log(data)
            oper.enumerate_file()
            ui.delete_succses()
            delete_menu_end_button()
    if menu_id == 2:
        search_menu_button()
    if menu_id == 0:
        main_menu_button()
    

def delete_menu_end_button():
    menu_id = ui.delete_menu_end()
    if menu_id == 1:
        delete_menu_button()
    if menu_id == 0:
        main_menu_button()
    

def update_menu_button():
    menu_id = ui.update_menu()
    if menu_id == 1:
        update_par_menu_button()
    if menu_id == 2:
        search_menu_button()
    if menu_id == 0:
        main_menu_button()
    else:
        ui.menu_input_error()
        update_menu_button()
def update_par_menu_button():
    number = ui.update_record_menu()
    record = oper.search_record(0, number)
    old = ';'.join(record[0])
    if record == []:
        update_par_menu_button()
    else:
        menu_id = ui.update_record_par_menu(record)
        if menu_id == 1:
            new = ';'.join(oper.update_record(int(number), 1, ui.name_input()))
        if menu_id == 2:
            new = ';'.join(oper.update_record(int(number), 2, ui.second_name_input()))
        if menu_id == 3:
            new = ';'.join(oper.update_record(int(number), 3 , ui.phone_number_input()))
        if menu_id == 4:
            new = ';'.join(oper.update_record(int(number), 4, ui.comment_input()))
        log.update_record_log(old,new)
        ui.update_sucsess()
        update_menu_end()

def update_menu_end():
    menu_id = ui.update_menu_end()
    if menu_id == 1:
        update_menu_button()
    if menu_id == 0:
        main_menu_button()
       
           


