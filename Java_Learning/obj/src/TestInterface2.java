public class TestInterface2 implements C {

    @Override
    public void testA() {
        System.out.println("This is a word: TestA");
    }

    public void testB() {
        System.out.println("This is a word: TestB");
    }

    public void testC() {
        System.out.println("This is a word: TestC");
    }

    public static void main(String[] args) {
        C c1 = new TestInterface2();
        c1.testA();
        c1.testB();
        c1.testC();
    }
}

interface A {
    void testA();
}

interface B {
    void testB();
}

interface C extends A, B{
    void testC();
}

