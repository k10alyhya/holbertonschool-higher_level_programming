#!/usr/bin/node

const n = parseInt(process.argv[2]);

if (isNaN(n)) {
  console.log('Missing size');
} else {
  let row = '';
  for (let i = 0; i < n; i++) {
    row += 'X';
  }
  for (let i = 0; i < n; i++) {
    console.log(row);
  }
}
