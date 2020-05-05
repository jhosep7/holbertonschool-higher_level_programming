#!/usr/bin/node
console.log(factorial(parseInt(process.argv[2])));
function factorial (Num) {
  if (!Num) {
    return 1;
  } else if (Num === 0) {
    return 1;
  } else {
    return Num * factorial(Num - 1);
  }
}
