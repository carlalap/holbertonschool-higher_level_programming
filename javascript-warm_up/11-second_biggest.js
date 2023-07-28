#!/usr/bin/node
// task 11 - script that searches the second biggest integer in the list of arguments.
const findSecondLargest = (numbers) => {
  if (numbers.length <= 1) {
    return 0;
  }

  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (let i = 0; i < numbers.length; i++) {
    const num = parseInt(numbers[i]);
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }

  return secondLargest;
};

const args = process.argv.slice(2);
const result = findSecondLargest(args);

console.log(result);
