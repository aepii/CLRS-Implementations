#include "StaticStack.hpp"

#include <iostream>
#include <vector>

template <typename T>
class StaticStack {
private:
  int _capacity;
  std::vector<T> stack;
  int _top;

public:
  StaticStack(int capacity) {
    _capacity = capacity;
  }
  
  bool isStackEmpty() const {

  }

  bool isStackFull() const {
    
  }

  int getCapacity() const {
    return _capacity;
  }

  int getSize() const {
    return _top + 1
  }

  push() {

  }

  pop() {
    
  }

  peek() {
    
  }
};