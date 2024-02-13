#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  let i;

  for (i = list.length - 1; i >= 0; i--) {
    const value = list[i];

    reversedList.push(value);
  }
  return reversedList;
};
