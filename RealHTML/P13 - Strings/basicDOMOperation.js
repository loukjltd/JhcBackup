'use strict'
function numTestCode(n){
    //自定义一个新的numTestCodeArray的数组
    const numTestCodeArray = [];
    //在给定的对应的位数中进行for循环随机生成几个数字
    for(let i = 1; i < n; i++){
        //使用Math.random随机生成[0, 1)的随机小数，通过乘以10后取整
        const num = parseInt(Math.random() * 10);
        //将生成后的随机数字放在该数组后方，此操作一共执行n遍
        numTestCodeArray.push(num);
    }
    //返回该生成好的数组
    return numTestCodeArray.join("");
}


//使用ASCII值生成包含大小写字母及数字的n位随机验证码，道理上同
function testCode(n){
    const testCodeArray = [];
    for(let i = 0; i < n; i++){
        const num = parseInt(Math.random() * 123);
        if(num >= 0 && num <=9){
            testCodeArray.push(num);
        }else if(num >= 97 && num <= 122 || num >= 65 && num <= 90){
            testCodeArray.push(String.fromCharCode(num));
        }else{
            i--;
        }
    }
    return testCodeArray.join("");
}


function buttonNumClick(){
    //拿到testNumCodeDiv这个<div>标签，放入destinationDiv中
    const destinationDiv = document.getElementById('testNumCodeDiv');
    //对该标签的内容进行赋值，使其能够响应随机生成数字验证码的函数
    destinationDiv.innerHTML = numTestCode(6);
}

function buttonClick(){
    const destinationDiv2 = document.getElementById('testCodeDiv');
    destinationDiv2.innerHTML = testCode(6);
}