#!/usr/bin/node

let n1 = process.argv[2];
n1 = parseInt(n1);
if (isNaN(n1)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${n1}`);
}
