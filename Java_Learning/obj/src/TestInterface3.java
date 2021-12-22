public class TestInterface3 {
    public static void main(String[] args) {
        TestA Ta = new TestA();
        Ta.default1();

        A1.staticMethod();
        TestA.staticMethod();

        TestB Tb = new TestB();
        Tb.default1();
    }
}

interface A1 {
    default void default1(){
        System.out.println("A1.default1");
    }
    default void default2(){
        System.out.println("A1.default2");
    }
    static void staticMethod() {
        System.out.println("A1.staticMethod");
    }
}

interface B1 {
    default void default1(){
        System.out.println("B1.default1");
    }
}

class TestA implements A1 {
    @Override
    public void default1() {
        System.out.println("TestA.default1");
    }

    static void staticMethod(){
        System.out.println("TestA.staticMethod");
    }
}

class TestB implements A1, B1 {
    @Override
    public void default1() {
        System.out.println("TestB.default1");
    }
}