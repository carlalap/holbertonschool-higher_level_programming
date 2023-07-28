#!/usr/bin/node
// task 10 - script that computes and prints a factorial

const num = parseInt(process.argv[2]);
function factorial (n) {
  if (!n) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(num));
