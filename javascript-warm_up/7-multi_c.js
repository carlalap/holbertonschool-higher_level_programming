#!/usr/bin/node
// task 7 - Write a script that prints x times “C is fun”

const num = parseInt(process.argv[2]);

if (!isNaN(num)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
