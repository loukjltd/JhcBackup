function lostBlurUserName(){
    const desUserName = document.getElementById('userName');
    const desUserNameSpan = document.getElementById('userNameSpan');

    const desValue = desUserName.value;

    if(desValue.length < 6 || desValue.length > 10){
        desUserNameSpan.innerHTML = 'The length should be 6 to 10 characters.'
    }else if(!isABC(desValue[0])){
        desUserNameSpan.innerHTML = 'The email address must start with an English letter.'
    }else{
        let allLegal = true;
        for(let i = 0; i < desValue.length; i++){
            if(!allLegalChar(desValue[i])){
                allLegal = false;
                break;
            }
        }
        if(allLegal){
            desUserNameSpan.innerHTML = 'Congratulations! The email address can be registered.'
        }else{
            desUserNameSpan.innerHTML = 'Email address must be composed of alphanumeric or underscore.'
        }
    }
}

function isABC(desString){
    return desString >= 'a' && desString <= 'z' || desString >= 'A' && desString <= 'Z';
}

function allLegalChar(charStr){
    return charStr >= "a" && charStr <= 'z' || charStr >= "A" && charStr <= "Z" || charStr >= "0" && charStr <= "9" || charStr === "_";
}

function getVerificationCode(n){
    const verificationCodeArray = [];
    for(let i = 0; i < n; i++){
        const num = parseInt(Math.random() * 123);
        if(num >= 0 && num <=9){
            verificationCodeArray.push(num);
        }else if(num >= 97 && num <= 122 || num >= 65 && num <= 90){
            verificationCodeArray.push(String.fromCharCode(num));
        }else{
            i--;
        }
    }
    alert('Hello, the verification code you requested is ' + verificationCodeArray.join("") + ', and will expire within 5 minutes.');
}
