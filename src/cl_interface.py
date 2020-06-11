# imports
import os
# modules
import directory as d 
import input_check as ic


option_list = ['callibrate', 'load', 'new']

def callibrate():
    pass

def load():
    pass
def new():
    '''
    1. list out folder to select photos to callibrate from
    '''    
    print('\nSelect the folder with the contents you wish to analyze:')
    dir_list = os.listdir()
    list_choices(dir_list)

    selected = select_choice(dir_list)
    # print(dir_list[selected])
    
def main_menu():
    print('Welcome to Photometry of Ordinary Objects. Select what you would like to do from the list below:')
    list_choices(option_list)

    # print(globals())
    globals()[option_list[select_choice(option_list)]]()

def list_choices(choice_list):
    for i in range(len(choice_list)):
        print(str(i) + ':', choice_list[i])

def select_choice(choice_list, error_message='Try again.'):
    selected_option = -1
    while selected_option not in range(len(choice_list)):
        selected_option = int(ic.filtered_input('int'))
        if selected_option not in range(len(option_list)):
            print(error_message)
    return selected_option 
    
# main_menu()
  