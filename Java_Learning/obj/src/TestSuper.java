public class TestSuper {
    public static void main(String[] args) {
        Child c1 = new Child();
        System.out.println(c1.num);
        c1.show();
    }
}

class Parent {
    int num = 300;

    public void show() {
        System.out.println("Show me something!");
    }

    public Parent() {
        System.out.println("Initialize Parent!");
    }
}

class Child extends Parent {
    int num = 1000;

    public Child() {
        System.out.println("Initialize Child!");
    }

    @Override
    public void show() {
        System.out.println("Show me your child!");
        super.show();
        System.out.println("New Value: " + num);
        System.out.println("Original: " + super.num);
    }
}
