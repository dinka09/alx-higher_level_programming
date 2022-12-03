#!/usr/bin/node
// executes x times a function.

exports.addMeMaybe = function (x, theFunction) {
  x++;
  theFunction(x);
};
