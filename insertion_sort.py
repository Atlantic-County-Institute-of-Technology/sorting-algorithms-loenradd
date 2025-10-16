

def insertsort(list):
    for this_variable_name_doesnt_matter in range((len(list))): # Do a bunch of passes to make triple sure that nothing screws up
        for i in range(len(list)):
            if i > 0:  # Prevents index error
                j = i - 1
            else:
                j = i
            temp = list[i]
            while temp < list[j]:
                list.insert(j, list.pop(i))  # If a value in the list is smaller than the one before it, pop it and insert it before the previous
                # print(list)
    print(list)


# chud_list = [20, 7, 21, 9, 6, 1, 33, 4, 32, 29]
#
# insertsort(chud_list)