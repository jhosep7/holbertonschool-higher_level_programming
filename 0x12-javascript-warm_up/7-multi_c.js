#!/usr/bin/node
const Num = parseInt(process.argv[2]);
if (!isNaN(Num)) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
