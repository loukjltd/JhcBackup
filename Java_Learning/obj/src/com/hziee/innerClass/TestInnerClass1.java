package com.hziee.innerClass;

public class TestInnerClass1 {
    public static void main(String[] args) {

        Outer1.Inner1 inner1 = new Outer1().new Inner1();
        inner1.test1();
    }
}
