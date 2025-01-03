#include "MergeSort.hpp"

#include <iostream>
#include <vector>

int main(){
  std::vector<int> myArray = {5, 2, 4, 6, 1, 3};
  std::cout << "Before Insertion Sort:" << std::endl;
  for(int element: myArray){
    std::cout << element << " "; 
  }
  std::cout << std::endl;

  mergeSort(myArray, 0, myArray.size() - 1);

  std::cout << "After Insertion Sort:" << std::endl;
  for (int element : myArray) {
      std::cout << element << " "; 
  }
  std::cout << std::endl;

  return 0;
}