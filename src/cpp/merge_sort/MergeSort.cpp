#include "MergeSort.hpp"

#include <iostream>
#include <vector>
#include <limits>

void mergeSort(std::vector<int>& array, int p, int r){
  if (p < r){
    int q = (p + r) / 2;
    mergeSort(array, p, q);
    mergeSort(array, q + 1, r);
    merge(array, p, q, r);
  }
}

void merge(std::vector<int>& array, int p, int q, int r){
  int n1 = q - p + 1;
  int n2 = r - q;

  std::vector<int> L(n1);
  std::vector<int> R(n2);

  std::copy(array.begin() + p, array.begin() + q + 1, L.begin());
  std::copy(array.begin() + q + 1, array.begin() + r + 1, R.begin());

  L.push_back(std::numeric_limits<int>::max());
  R.push_back(std::numeric_limits<int>::max());

  int i = 0, j = 0;

  for(int k = p; k <= r; ++k){
    if (L[i] <= R[j]){
      array[k] = L[i];
      ++i;
    }else{
      array[k] = R[j];
      ++j;
    }
  }
}