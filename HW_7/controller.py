# import view
# from logger import log
# import model

# def start():
#     '''Стартовая функция'''
#     view.greetings()
#     while True:
#         match view.menu():
#             case '1': # Показать справочник
#                 view.print_book(model.get_data())
#             case '2': # Добавить запись
#                 model.add_data(view.input_data())
#             case '3': # Выход
#                 break

import view
from logger import log
import model


@log
def start():
    """Стартовая функция"""
    view.greatings()
    while True:
        match view.menu():
            case 0:
                break
            case 1:
                view.print_book(model.get_data())
            case 2:
                model.add_data(view.add_record())
            case 3:
                model.add_data(view.editor(model.get_data_id(view.request_id())))
            case 4:
                view.print_book(model.get_data_last_name(view.request_last_name()))
