package com.hziee;

public class Test03 {
    public static void main(String[] args) {
        String[] a = {"AliPay", "JD", "NetEase", "Tencent"};
        String[] b = new String[6];

        System.arraycopy(a, 1, b, 0, 2);

        for(String t: b){
            System.out.println(t);
        }
    }
}
