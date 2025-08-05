#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
  process.exit(0);
}

let max = -Infinity;
let secondMax = -Infinity;

for (const num of args) {
  if (num > max) {
    secondMax = max;
    max = num;
  } else if (num > secondMax && num < max) {
    secondMax = num;
  }
}

console.log(secondMax === -Infinity ? 0 : secondMax);
