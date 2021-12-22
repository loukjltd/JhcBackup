public class TestInterface {
    public static void main(String[] args) {
        Angel a1 = new Angel();
        a1.fly();
        a1.helpOthers();
        System.out.println();
        Interface2 i1 = new Angel();
        i1.helpOthers();

    }
}

interface Interface1 {
    int FLU_HEIGHT = 100;
    void fly();
}

interface Interface2 {
    void  helpOthers();
}

class Angel implements Interface1, Interface2 {
    @Override
    public void fly() {
        System.out.println("I love flying.");
    }

    @Override
    public void helpOthers() {
        System.out.println("I love helping others!");
    }
}

class BirdMan implements Interface1 {
    @Override
    public void fly() {
        System.out.println("I can only fly.");
    }
}