#!/usr/bin/node

module.exports.callMeMoby = function (x, theFunction) {
  let i;
  for (i = 0; i < x; i++) {
    theFunction();
  }
};
