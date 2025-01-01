#include "InsertionSort.hpp"

#include <iostream>
#include <vector>

void insertionSort(std::vector<int>& array){
  for(size_t j = 1; j < array.size(); ++j){
    int key = array[j];
    int i = j - 1;

    while(j >= 0 && array[i] > key){
      array[i + 1] = array[i];
      i -= 1;
    }
    array[i + 1] = key;
  }
}