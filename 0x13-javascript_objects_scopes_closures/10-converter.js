#!/usr/bin/node
exports.converter = function (base) {
  return function (Mybase) {
    return Mybase.toString(base);
  };
};
