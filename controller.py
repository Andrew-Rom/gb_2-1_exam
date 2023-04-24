import ui_text as ui
import logger as log
import actions as db


def operations():
    while True:
        ui.show_menu()
        user_command = input(ui.select_msg)
        match user_command:
            case '0':
                log.logging.info('Stop program')
                ui.show_exit_message()
                exit()
            case '1':
                log.logging.info('Show all notes')
                db.show_all()
            case '2':
                log.logging.info('Selected by ID')
                db.search_by_id()
            case '3':
                log.logging.info('Selected by date')
                db.search_by_date()
            case '4':
                log.logging.info('Enter new note')
                db.create_note()
            case '5':
                db.change_note()
            case '6':
                db.del_note()
            case _:
                log.logging.error('Incorrect selection')
                ui.show_error_input_msg()
                continue
