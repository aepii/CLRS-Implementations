"""
In-place sorting algorithm which compares a key element with elements
to its left and shifting larger elements to the right until the key is in the correct place.
"""
def insertion_sort(array, ascending=True):
    # Build sorted array one element at a time. 
    # Assume the first element is already "sorted".
    for j in range(1, len(array)):  
        key = array[j] # Key element to be inserted into the sorted array.
        i = j - 1 # Index to the left of the key element.

        # If sorting in ascending order:
        # Check elements to the left of the key element until 
        # the key element is less than or equal to the compared element.

        # If sorting in descending order:
        # Check elements to the left of the key element until 
        # the key element is greater than the compared element.
        while i >= 0 and (array[i] > key if ascending else array[i] <= key): 
            array[i + 1] = array[i] # Element that is being compared is shifted to the right.
            i -= 1 # Start comparing with the next element on the key's left.
        array[i + 1] = key # Place the key element in the correct sorted position.

    return array # Return the array.

"""
Implementation where the ascending boolean is not re-evaluated on every iteration:

def insertion_sort(array, ascending=True):
    if ascending:
        for j in range(1, len(array)):  
            key = array[j]
            i = j - 1
            while i >= 0 and array[i] > key:
                array[i + 1] = array[i]
                i -= 1
            array[i + 1] = key
    else:
        for j in range(1, len(array)):  
            key = array[j]
            i = j - 1
            while i >= 0 and array[i] <= key:
                array[i + 1] = array[i]
                i -= 1
            array[i + 1] = key
    
    return array
"""