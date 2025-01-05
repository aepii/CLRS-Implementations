#include "BubbleSort.hpp"

#include <iostream>
#include <utility>

void bubbleSort(std::vector<int>& array){
  for(int i = 0; i < array.size() - 1; ++i){
    for(int j = array.size() - 1; j > i; --j){
      if(array[j] < array[j - 1]){
        std::swap(array[j], array[j - 1]);
      }
    }
  }
}