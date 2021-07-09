package com.jhc.inherit;

public class TestExtends {
    public static void main(String[] args) {
        Students s1 = new Students();
        s1.study();

        Students s2 = new Students("Sean", 179, 75, "Networking");
        s2.showInfo();
    }
}

class Person {
    String name;
    int height;
    int weight;

    public void rest() {
        System.out.println("Take a break!");
    }
}

class Students extends Person {
    String major;

    public void study() {
        System.out.println("Study for a while!");
    }
    public void showInfo() {
        System.out.println("Hi! My name is " + name + ".");
        System.out.println("I'm " + height + " meters tall and " + weight + " kg.");
        System.out.println("My most interested major is " + major + ".");
    }

    public Students() {

    }

    public Students(String name, int height, int weight, String major) {
        this.name = name;
        this.height = height;
        this.weight = weight;
        this.major = major;
    }
}
