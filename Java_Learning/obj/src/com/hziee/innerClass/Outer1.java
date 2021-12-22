package com.hziee.innerClass;

public class Outer1 {
    private int age = 18;
    public void show(){
        System.out.println("age: " + 18);
    }

    class Inner1 {
        private int id = 10001;
        private int age = 18;

        public void test1(){
            System.out.println("inner1.test1");
            System.out.println("Inside age: " + age);
            System.out.println("Outside age: " + Outer1.this.age);
            Outer1.this.show();
        }
    }
}
