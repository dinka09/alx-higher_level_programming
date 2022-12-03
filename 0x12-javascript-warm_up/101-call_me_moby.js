#!/usr/bin/node
// executes x times a function.

exports.callMeMoby = function (x, theFunction) {
  x++;
  theFunction(x);
};
