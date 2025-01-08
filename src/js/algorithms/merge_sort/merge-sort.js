export function mergeSort(array, p, r) {
  if (p < r) {
    const q = Math.floor((p + r) / 2)
    mergeSort(array, p, q);
    mergeSort(array, q + 1, r);
    merge(array, p, q, r);
  }
}

function merge(array, p, q, r) {
  const n1 = q - p + 1;
  const n2 = r - q;

  let L = [...array.slice(p, q + 1), Infinity];
  let R = [...array.slice(q + 1, r + 1), Infinity];

  let i = 0, j = 0;

  for(let k = p; k <= r; ++k) {
    if(L[i] <= R[j]) {
      array[k] = L[i];
      ++i;
    }else {
      array[k] = R[j];
      ++j;
    }
  }
}