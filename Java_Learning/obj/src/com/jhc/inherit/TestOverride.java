package com.jhc.inherit;

public class TestOverride {
    public static void main(String[] args) {
        Horse h1 = new Horse();
        h1.run();
        h1.stop();
        Plane p1 = new Plane();
        p1.run();
        p1.stop();
    }
}

class Vehicle {
    public void run() {
        System.out.println("Run!");
    }

    public void stop() {
        System.out.println("Stop!");
    }
}

class Horse extends Vehicle {
    public void run() {
        System.out.println("I can't run...");
    }
}

class Plane extends Vehicle {
    public void run() {
        System.out.println("I can't run...");
    }
}
