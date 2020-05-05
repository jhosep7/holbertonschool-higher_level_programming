#!/usr/bin/node
const slice = process.argv.slice(2).sort((a, b) => b - a)[1];
console.log(process.argv.length < 4 ? 0 : slice);
