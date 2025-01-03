import math

def merge_sort(array, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(array, p, q) 
        merge_sort(array, q + 1, r)
        merge(array, p, q, r) 

def merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    left_array = array[p:q+1] + [math.inf]
    right_array = array[q+1:r+1] + [math.inf]

    i = j = 0

    for k in range(p, r + 1):
        print(left_array)
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1