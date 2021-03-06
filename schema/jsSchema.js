'use strict'; // code generated by pbf v3.2.1

// Dot ========================================

var Dot = exports.Dot = {};

Dot.read = function (pbf, end) {
    return pbf.readFields(Dot._readField, {val: []}, end);
};
Dot._readField = function (tag, obj, pbf) {
    if (tag === 1) pbf.readPackedVarint(obj.val, true);
};
Dot.write = function (obj, pbf) {
    if (obj.val) pbf.writePackedVarint(1, obj.val);
};
