package com.jhc.polymorphism;

public class Animal {
    public void shout() {
        System.out.println("Shout!");
    }
}

class Dog extends Animal {
    @Override
    public void shout() {
        System.out.println("Dog Shout!");
    }
    public void watchDoor() {
        System.out.println("Watch the Door!");
    }
}


class Cat extends Animal {
    @Override
    public void shout() {
        System.out.println("Cat Shout!");
    }
}
