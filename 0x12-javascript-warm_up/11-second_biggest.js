#!/usr/bin/node

const { argv } = require('process');

if (argv.length <= 3) {
  console.log(0);
} else {
  const nums = argv.slice(2).map(Number).sort((a, b) => b - a);
  console.log(nums[1]);
}
