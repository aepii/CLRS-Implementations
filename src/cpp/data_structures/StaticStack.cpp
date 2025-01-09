#include "StaticStack.hpp"

#include <iostream>
#include <vector>

template <typename T>
class StaticStack {
private:
  int _capacity;
  std::vector<T> _stack;
  int _top;

public:
  StaticStack(int capacity) 
    : _capacity(capacity), _top(-1), _stack(_capacity) { 
  }
  
  bool isStackEmpty() const {
    return _top == -1;
  }

  bool isStackFull() const {
    return _top == _capacity - 1;
  }

  int getCapacity() const {
    return _capacity;
  }

  int getSize() const {
    return _top + 1;
  }

  void push(const T& x) {
    if(isStackFull()) {
      throw std::overflow_error("Stack is full.");
    }
    _stack[++_top] = x;
  }

  T pop() {
    if(isStackEmpty()) {
      throw std::overflow_error("Stack is empty.");
    }
    return _stack[_top--];
  }

  T peek() const {
    if(isStackEmpty()) {
      throw std::overflow_error("Stack is empty.");
    }
    return _stack[_top];
  }
};