package com.jhc.polymorphism;

public class TestPolymorphism {
    public static void main(String[] args) {
        Dog d1 = new Dog();
        animalShout(d1);
        Cat c1 = new Cat();
        animalShout(c1);

        Dog a1 = new Dog();
        a1.shout();
        a1.watchDoor();
    }

    static void animalShout(Animal a) {
        a.shout();
    }
}
