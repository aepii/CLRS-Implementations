import { mergeSort } from "./merge-sort.js";

function main() {
  const myArray = [5, 2, 4, 6, 1, 3];
  console.log(`Before Insertion Sort: ${myArray}`);
  mergeSort(myArray);
  console.log(`After Insertion Sort: ${myArray}`);
}

main();