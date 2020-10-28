//存储需要被过滤的敏感词，并使用正则表达式
const sensitiveArray = [/tmd/ig, /nm/ig];

//建立点击「发布」按钮时相应的函数操作
function buttonClick(){
    //链接对应的id，并将textBox中的值放入desText中
    const desText = document.getElementById('textBox');
    //链接对应的id，并将msgBox中的值放入desMsg中
    const desMsg = document.getElementById('msgBox');

    //将文本框中的字赋值到一个新的变量desValue中，用于存储过滤
    let desValue = desText.value;
    //用for循环遍历一遍所有文字
    for(let i = 0; i < sensitiveArray.length; i++){
        //检测到有包含sensitiveArray中的值时，将其替换为*并重新赋值给自己
        desValue = desValue.replace(sensitiveArray[i], '*');
    }
    //将最终已经过滤好了的文字放在Msg消息框中
    desMsg.innerHTML = desValue;
    //同时清空之前的输入框
    desText.value = '';
}