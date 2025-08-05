#!/usr/bin/node

const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let i = 0;
let output = '';

while (i < languages.length) {
  output += languages[i] + (i === languages.length - 1 ? '' : '\n');
  i++;
}

console.log(output);
