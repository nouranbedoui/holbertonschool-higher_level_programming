#!/usr/bin/node

const args = process.argv.slice(2);
const size = parseInt(args[0], 10);

if (!args[0] || isNaN(size) || size <= 0) {
  console.log('Missing size');
} else {
  let i = 0;
  const line = 'X'.repeat(size);
  while (i < size) {
    console.log(line);
    i++;
  }
}
