package com.jhc.inherit;

public class TestComposition {
    public static void main(String[] args) {
        Teacher t1 = new Teacher("Tina", 165, 55, "EnglishForSpecialPurpose");
        t1.teach();
        t1.showInfo();

        Teacher t2 = new Teacher();
        t2.teach();
        t2.showInfo();

        PC pc1 = new PC();
        pc1.cpu.calculate();
        pc1.memory.store();
    }
}

class Teacher {
    Person examplePerson = new Person();
    String major;

    public void teach() {
        System.out.println("Teaching...");
    }
    public void showInfo() {
        System.out.println(examplePerson.name + examplePerson.height + examplePerson.weight + major);
    }

    public Teacher() {

    }

    public Teacher(String name, int height, int weight, String major) {
        this.examplePerson.name = name;
        this.examplePerson.height = height;
        this.examplePerson.weight = weight;
        this.major = major;
    }
}

class CPU {
    void calculate() {
        System.out.println("Doing Calculation.");
    }
}

class Memory {
    void store() {
        System.out.println("Store Information.");
    }
}

class PC {
    CPU cpu = new CPU();
    Memory memory = new Memory();
}