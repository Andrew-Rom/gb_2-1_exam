def show_menu():
    print("\n"
          "************************************************************\n"
          "********************* Welcome to NOTES *********************\n"
          "************************************************************\n"
          "* 1 - Show a list of all notes                             *\n"
          "* 2 - Find the note by ID and show it                      *\n"
          "* 3 - Find all notes by creation date and the lis of them  *\n"
          "* 4 - Add new note                                         *\n"
          "* 5 - Edit a note                                          *\n"
          "* 6 - Delete a note                                        *\n"
          "* 0 - Exit                                                 *\n"
          "************************************************************")


def show_exit_message():
    print("\n"
          "*************************\n"
          "*** NOTES was stopped ***\n"
          "*************************\n")


def show_error_menu_message():
    print('Error selection. Try again, please.')


def show_error_file_message():
    print('Sorry, the database file does not exist or was corrupted.')
