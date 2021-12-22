package com.hziee.innerClass;

public class TestLocalInnerClass {
    public void show(){
        System.out.println("step1");

        class Inner3 {
            public void run(){
                System.out.println("Inner3.run");
            }
        }

        new Inner3().run();
    }

    public static void main(String[] args) {
        new TestLocalInnerClass().show();
    }
}
