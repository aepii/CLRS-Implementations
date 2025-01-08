def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]

"""
Can be optimized with an early exit which prevents unnecessary passes:

def bubble_sort(array):
    for i in range(len(array) - 1):
        swapped = False
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                swapped = True

        if not swapped:
            break
"""