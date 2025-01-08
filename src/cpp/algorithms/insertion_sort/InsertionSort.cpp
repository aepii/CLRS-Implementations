#include "InsertionSort.hpp"

#include <iostream>
#include <vector>

/*
In-place sorting algorithm which compares a key element with elements
to its left and shifting larger elements to the right until the key is in the correct place.
*/
void insertionSort(std::vector<int>& array, bool ascending) {
  // Build sorted array one element at a time. 
  // Assume the first element is already "sorted".
  for(int j = 1; j < array.size(); ++j) {
    int key = array[j]; // Key element to be inserted into the sorted array.
    int i = j - 1; // Index to the left of the key element.

    // If sorting in ascending order:
    // Check elements to the left of the key element until 
    // the key element is less than or equal to the compared element.

    // If sorting in descending order:
    // Check elements to the left of the key element until 
    // the key element is greater than the compared element.
    
    while(i >= 0 && (ascending ? array[i] > key : array[i] <= key)) {
      array[i + 1] = array[i]; // Element that is being compared is shifted to the right.
      i -= 1; // Start comparing with the next element on the key's left.
    }
    array[i + 1] = key; // Place the key element in the correct sorted position.
  }
}