Unit тесты
Для модуля user_interface.py
- функция menu() -> проверить, что возвращает валидное значение
- функция search_menu() -> проверить, что возвращает валидное значение
- функция search_menu_end() -> проверить, что возвращает валидное значение
- функция add_record_menu_end() -> проверить, что возвращает валидное значение
- функция delete_menu() -> проверить, что возвращает валидное значение
- функция delete_menu_end() -> проверить, что возвращает валидное значение
- функция delete_menu() -> проверить, что возвращает валидное значение
- функция delete_menu_end() -> проверить, что возвращает валидное значение
- функция update_menu() -> проверить, что возвращает валидное значение
- функция update_record_menu() -> проверить, что возвращает валидное значение
- функция update_record_par_menu -> проверить, что возвращает валидное значение
- функция update_menu_end() -> проверить, что возвращает валидное значение
Для модуля controller.py
- main_menu_button() -> проверить, что вызывает валидную функцию, используем заглушку
- search_menu_button() -> проверить, что вызывает валидную функцию, используем заглушку
- add_record_menu_button() -> проверить, что вызывает валидную функцию, используем заглушку
- delete_menu_button() -> проверить, что вызывает валидную функцию, используем заглушку
- update_menu_button() -> проверить, что вызывает валидную функцию, используем заглушку
Для модуля operations.py
Интеграционные тесты:
- test_add_record() -> проверить, что добавляет запись в БД, используем заглушку fake_add_record
- test_delete_record() -> проверить, что удаляет запись из БД, используем заглушку fake_delete_record
- test_update_record() -> проверить, что обновляет запись в БД, используем заглушку fake_update_record
- test_search_record() -> проверить, что ищет запись в БД, используем заглушку fake_search_record
e2e тесты:
- test_add_update_record() -> проверить, что добавляет и обновляет запись в БД, используем заглушку fake_add_record, fake_update_record
- test_add_delete_record() -> проверить, что добавляет и удаляет запись в БД, используем заглушку fake_add_record, fake_delete_record, а также производит логирование