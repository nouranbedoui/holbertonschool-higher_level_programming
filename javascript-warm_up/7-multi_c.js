#!/usr/bin/node

const args = process.argv.slice(2);
const times = parseInt(args[0], 10);

if (!times || times < 1) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < times) {
    console.log('C is fun');
    i++;
  }
}
