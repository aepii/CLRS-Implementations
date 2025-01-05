### 
1. Loop through all elements except the first element.
2. Compare the key element with elements on its left until a correct position is found.

### Ascending Order Psuedo Code
INSERTION-SORT-ASC(A)
for j = 2 to A.length
  key = A[j]
  i = j - 1
  while i > 0 and A[i] > key
    A[i + 1] = A[i]
    i = i - 1
  A[i + 1] = key

### Descending Order Psuedo Code
INSERTION-SORT-DESC(A)
for j = 2 to A.length
  key = A[j]
  i = j - 1
  while i > 0 and A[i] <= key
    A[i + 1] = A[i]
    i = i - 1
  A[i + 1] = key