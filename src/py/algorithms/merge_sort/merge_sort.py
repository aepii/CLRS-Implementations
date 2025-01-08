import math

"""
Sorting algorithm which utilizes the divide-and-conquer paradigm by
dividing an array into subarrays while recursively sorting each subarray.
"""
def merge_sort(array, p, r):
    # Divide the array if the left index is smaller than the right index.
    if p < r: 
        q = (p + r) // 2 # Compute the midpoint of the array.
        merge_sort(array, p, q) # Divide into a left subarray.
        merge_sort(array, q + 1, r) # Divide into a right subarray.
        merge(array, p, q, r) # Sort the contents of the subarray.

def merge(array, p, q, r):
    n1 = q - p + 1 # Compute the size of the left subarray.
    n2 = r - q # Compute the size of the right subarray.

    left_array = array[p:q+1] + [math.inf] # Copy the left half of the array into a left subarray plus a sentinel value.
    right_array = array[q+1:r+1] + [math.inf] # Copy the right half of the array into a right subarray plus a sentinel value.

    # The sentinel values ensure the indices, i and j, do not
    # go out of bounds which gaurantees all elements to be exhausted.

    i = j = 0 # Initialize indices, i and j, to zero.
    
    # Iterate through all elements from the left to the right subarrays.
    for k in range(p, r + 1):
        # If the element from the left array is smaller than the element from the right array.
        if left_array[i] <= right_array[j]: 
            array[k] = left_array[i] # Place the element from the left array into its correct position.
            i += 1 # Increment the left array's pointer.
        # Else, the element from the right array must be smaller than the element from the left array.
        else:
            array[k] = right_array[j] # Place the element from the right array into its correct position.
            j += 1 # Increment the right array's pointer.

"""
To sort in descending order, simply negate the sentinel values:

left_array = array[p:q+1] + [-math.inf]
right_array = array[q+1:r+1] + [-math.inf]

additionally, the comparison logic should be flipped:

if left_array[i] > right_array[j]:
    array[k] = left_array[i]
    i += 1
else:
    array[k] = right_array[j]
    j += 1
"""