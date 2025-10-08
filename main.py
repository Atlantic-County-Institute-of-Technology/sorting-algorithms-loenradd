# Leonard DeMarco, 10/8/25 - 10/00/25, sorting-algorithms.py

from bubble_sort import *
import random
import os

list_to_convert = [0]
create_random_list = True

def create_list():
    print(f"{list_to_convert} \n[!] This is your current list.\n")
    try:
        added_number = int(input("[!] Input a number to add it to the list. Input anything else to finish : "))
        list_to_convert.insert(added_number)
        create_list()
    except ValueError:
        pass

print(
    "[1] Generate Random List\n[2] Create Custom List"
)
while True:
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
    except ValueError:
        print("[!] Please select a valid option.")
