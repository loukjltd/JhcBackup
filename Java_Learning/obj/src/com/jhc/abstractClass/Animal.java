package com.jhc.abstractClass;

public abstract class Animal {
    public abstract void shout();
    public void sleep(){
        System.out.println("Animal.sleep");
    }

    public static void main(String[] args) {
        Dog d1 = new Dog();
        d1.shout();
        d1.sleep();
        d1.watchDoor();

        Cat c1 = new Cat();
        c1.shout();
        c1.sleep();
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
