# Leonard DeMarco, 10/8/25 - 10/00/25, sorting-algorithms.py

from bubble_sort import *
from insertion_sort import *
from selection_sort import *
import random
import os

list_to_convert = [0]
create_random_list = True
phase_one = True
phase_two = True
def create_list():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{list_to_convert} \nThis is your current list.\n")
    try:
        added_number = int(input("[!] Input a number to add it to the list. Input anything else to finish : "))
        list_to_convert.append(added_number)
        create_list()
    except ValueError:
        pass


while phase_one:
    # i love you terminal clear command
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[1] Generate Random List\n[2] Create Custom List\n[3] Begin Sorting")
    try:
        list_option = int(input("[-] Select an option: "))

        match list_option:
            case 1:
                while create_random_list:
                    try:
                        list_length = int(input("[-] Input how long the list should be : "))
                        if list_length <= 0:
                            list_length = abs(list_length)
                            print("[!] Value is less than 0. Absolute value applied.")
                        list_to_convert = [random.randint(0,100) for i in range(list_length)]
                        print(list_to_convert)
                        create_random_list = False
                    except ValueError:
                        print("[!] Please input a valid integer.")
            case 2:
                create_list()
            case 3:
                phase_one = False
    except ValueError:
        print("[!] Please select a valid option.")

while phase_two:
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        print("[1] Bubble Sort\n[2] Insertion Sort\n[3] Selection Sort\n")
        sort_option = int(input("[!] Select an option"))
        match sort_option:
            case 1:
                bubblesort(list_to_convert)
            case 2:
                insertsort(list_to_convert)
            case 3:
                selectsort(list_to_convert)
    except ValueError:
        print("[!] Please select a valid option.")

