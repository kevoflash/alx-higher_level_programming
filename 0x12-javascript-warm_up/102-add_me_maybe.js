#!/usr/bin/nodes
exports.addMeMaybe = function (number, theFunction) {
  theFunction.call(this, number + 1);
};
