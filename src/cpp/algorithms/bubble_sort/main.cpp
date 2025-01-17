#include "BubbleSort.hpp"

#include <iostream>
#include <vector>

int main() {
  std::vector<int> myArray = {5, 2, 4, 6, 1, 3};
  std::cout << "Before Insertion Sort:" << std::endl;
  for(int element: myArray) {
    std::cout << element << " "; 
  }
  std::cout << std::endl;

  bubbleSort(myArray);

  std::cout << "After Insertion Sort:" << std::endl;
  for (int element : myArray) {
      std::cout << element << " "; 
  }
  
  return 0;
}