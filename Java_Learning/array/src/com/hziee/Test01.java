package com.hziee;

public class Test01 {
    public static void main(String[] args) {

        int[] a = new int[5];
        int b[] = new int[3];
        int[] c = {100, 200, 300, 400, 500};

        System.out.println("initial value: " + a[0]);


        for(int i = 0; i <a.length; i++) {
            a[i] = 10 + 10 * i;
        }

        for(int i = 0; i < a.length; i++) {
            System.out.println("final value: " + i + ", " + a[i]);
        }

        for(int t: c) {
            System.out.println(t);
        }

    }
}
