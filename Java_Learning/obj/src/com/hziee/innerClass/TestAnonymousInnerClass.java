package com.hziee.innerClass;

public class TestAnonymousInnerClass {

    public void test(A3 a){
        System.out.println("TestAnonymousInnerClass.test");
        a.run();
    }

    public static void main(String[] args) {
        TestAnonymousInnerClass Tc = new TestAnonymousInnerClass();
        Tc.test(new A3() {
            @Override
            public void run() {
                System.out.println("TestAnonymousInnerClass.run");
            }
        });
    }

}

interface A3 {
    void run();
}
