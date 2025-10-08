#Bubble Sort 10/8/25


def bubblesort(list):
    outer = 0
    inner = 0
    for i in range(len(list) - 1):
        outer += 1
        for j in range(len(list) -i -1):
            inner += 1

            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


