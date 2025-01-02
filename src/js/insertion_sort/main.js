import { insertionSort } from "./insertion-sort.js";

function main() {
  const myArray = [5, 2, 4, 6, 1, 3];
  console.log(`Before Insertion Sort: ${myArray}`);
  insertionSort(myArray);
  console.log(`After Insertion Sort: ${myArray}`);

  const myArray2 = [5, 2, 4, 6, 1, 3];
  console.log(`Before Insertion Sort: ${myArray}`);
  insertionSort(myArray, false);
  console.log(`After Insertion Sort: ${myArray}`);
}

main();