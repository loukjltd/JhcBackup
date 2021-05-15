// 强制转换为布尔型：非0即真、非空即真。
alert(Boolean(0)); // false
alert(Boolean(123)); // true
alert(Boolean(-1)); // ture
alert(Boolean('hello')); // true
alert(Boolean('')); // false
alert(Boolean(null)); // false
alert(Boolean(undefined)); // false
alert(Boolean(NaN)); // false

// 强制转换为数字：只有数字才是数字，其它的都是NaN
alert(Number('100')); // 100
alert(Number('100a')); // NaN

// 取整
alert(parseInt('10a0b3c')); // 10
alert(parseInt('3.14')); // 3

// 取浮点数
alert(parseFloat('3.14abc')) // 3.14

// 进制转换
alert(parseInt('110100', 2)) // 二进制转十进制：52
alert(parseInt('64', 8)) // 八进制转十进制：52
alert(parseInt('34', 16)) //十六进制转十进制：52
