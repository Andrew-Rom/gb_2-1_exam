import ui_text as ui
import logger as log

def operations():
    while True:
        ui.show_menu()
        user_command = input(ui.show_select_message)
        if user_command == '0':
            log.logging.info('Stop program')
            ui.show_exit_message()
            exit()
        elif user_command == '1':
            pass
            log.logging.info('Show all notes')
            ## print(tabulate(db.read_file()))
            input(ui.show_waiting_message)
        elif user_command == '2':
            pass
            log.logging.info('Selected by ID')
            ## act.searching_by_id()
        elif user_command == '3':
            pass
            log.logging.info('Selected by date')
            ## act.searching_by_date()
        elif user_command == '4':
            pass
            log.logging.info('Enter new note')
            ## change_db.create_note()
        elif user_command == '5':
            pass
            ## change_db.change_note()
        elif user_command == '6':
            pass
            ## change_db.del_note()
        elif user_command not in ['0', '1', '2', '3', '4', '5', '6']:
            log.logging.error('Incorrect selection')
            ui.show_error_menu_message()
            continue
        else:
            break
