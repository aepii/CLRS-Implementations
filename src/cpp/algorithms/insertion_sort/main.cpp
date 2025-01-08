#include "InsertionSort.hpp"

#include <iostream>
#include <vector>

int main() {
  std::vector<int> myArray = {5, 2, 4, 6, 1, 3};
  std::cout << "Before Insertion Sort:" << std::endl;
  for(int element: myArray) {
    std::cout << element << " "; 
  }
  std::cout << std::endl;

  insertionSort(myArray);

  std::cout << "After Insertion Sort:" << std::endl;
  for (int element : myArray) {
      std::cout << element << " "; 
  }
  std::cout << std::endl;

  std::vector<int> myArray2 = {5, 2, 4, 6, 1, 3};
  std::cout << "Before Insertion Sort:" << std::endl;
  for(int element: myArray2) {
    std::cout << element << " "; 
  }
  std::cout << std::endl;

  insertionSort(myArray2, false);

  std::cout << "After Insertion Sort:" << std::endl;
  for (int element : myArray2) {
      std::cout << element << " "; 
  }
  std::cout << std::endl;
  
  return 0;
}