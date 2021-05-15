// 1. 入职薪资10K，每年涨入职薪资的5%，50年后薪资多少？
// 2. 为抵抗洪水，战士连续作战89小时，共多少天多少小时？
// 3. 华氏摄氏度80度转换成摄氏度（摄氏度=5/9*(华氏摄氏度-32)）。
// 4. 给定一个三位数，计算它的百位数、十位数、个位数。

const enterSalary = 10000;
let finalSalary;
finalSalary = enterSalary * (1 + 0.05 * 50);
alert('50年后的薪资为' + finalSalary + '元。');

const totalHour = 89;
let remainDay;
let remainHour;
remainDay = Math.trunc(totalHour / 24);
remainHour = totalHour % 24;
alert('共连续作战' + remainDay + '天又' + remainHour + '小时。')

const fDegree = 80;
let cDegree;
cDegree = Math.round((fDegree - 32) * (5 / 9));
alert('80华氏摄氏度为' + cDegree + '摄氏度。')

const hundredNumber = 321;
let theOnesPlace;
let theTensPlace;
let theHundredsPlace;
theOnesPlace = hundredNumber % 10;
theTensPlace = Math.trunc(hundredNumber % 100 / 10);
theHundredsPlace = Math.trunc(hundredNumber / 100);
alert(hundredNumber + '的个位数是' + theOnesPlace + '，十位数是' + theTensPlace + '，百位数是' + theHundredsPlace + '。')