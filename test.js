var _pyfunc_int = function (x, base) { // nargs: 1 2
    if(base !== undefined) return parseInt(x, base);
    return x<0 ? Math.ceil(x): Math.floor(x);
};
var _pyfunc_str = String;
var _pymeth_append = function (x) { // nargs: 1
    if (!Array.isArray(this)) return this.append.apply(this, arguments);
    this.push(x);
};
var _pymeth_split = function (sep, count) { // nargs: 0, 1 2
    if (this.constructor !== String) return this.split.apply(this, arguments);
    if (sep === '') {var e = Error('empty sep'); e.name='ValueError'; throw e;}
    sep = (sep === undefined) ? /\s/ : sep;
    if (count === undefined) { return this.split(sep); }
    var res = [], i = 0, index1 = 0, index2 = 0;
    while (i < count && index1 < this.length) {
        index2 = this.indexOf(sep, index1);
        if (index2 < 0) { break; }
        res.push(this.slice(index1, index2));
        index1 = index2 + sep.length || 1;
        i += 1;
    }
    res.push(this.slice(index1));
    return res;
};
var _pymeth_splitlines = function (keepends) { // nargs: 0 1
    if (this.constructor !== String) return this.splitlines.apply(this, arguments);
    keepends = keepends ? 1 : 0
    var finder = /\r\n|\r|\n/g;
    var i = 0, i2, isrn, parts = [];
    while (finder.exec(this) !== null) {
        i2 = finder.lastIndex -1;
        isrn = i2 > 0 && this[i2-1] == '\r' && this[i2] == '\n';
        if (keepends) parts.push(this.slice(i, finder.lastIndex));
        else parts.push(this.slice(i, i2 - isrn));
        i = finder.lastIndex;
    }
    if (i < this.length) parts.push(this.slice(i));
    else if (!parts.length) parts.push('');
    return parts;
};
var main;
main = function flx_main () {
    var csv, data, i, keys, split, stub1_, stub1_i0, stub1_iter0, stub1_x, stub2_, stub2_i0, stub2_iter0, stub2_x, value, values;
    csv = (open("test.csv", "r").read)();
    data = [];
    keys = [];
    values = [];
    split = _pymeth_splitlines.call(csv);
    for (i = 0; i < split.length; i += 1) {
        _pymeth_append.call(keys, (_pymeth_split.call(split[i], ",")[0]));
        _pymeth_append.call(values, (_pymeth_split.call(split[i], ",")[1]));
    }
    stub1_ = [];stub1_iter0 = keys;if ((typeof stub1_iter0 === "object") && (!Array.isArray(stub1_iter0))) {stub1_iter0 = Object.keys(stub1_iter0);}for (stub1_i0=0; stub1_i0<stub1_iter0.length; stub1_i0++) {stub1_x = stub1_iter0[stub1_i0];{stub1_.push(_pyfunc_int(stub1_x));}}
    keys = stub1_;
    stub2_ = [];stub2_iter0 = values;if ((typeof stub2_iter0 === "object") && (!Array.isArray(stub2_iter0))) {stub2_iter0 = Object.keys(stub2_iter0);}for (stub2_i0=0; stub2_i0<stub2_iter0.length; stub2_i0++) {stub2_x = stub2_iter0[stub2_i0];{stub2_.push(_pyfunc_int(stub2_x));}}
    values = stub2_;
    for (i = 0; i < keys.length; i += 1) {
        for (value = 0; value < values[i]; value += 1) {
            _pymeth_append.call(data, keys[i]);
        }
    }
    console.log((_pyfunc_str(random.choice(data))));
    return null;
};
main();