package com.jhc.test3;
import com.jhc.test.Car;
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Car c1 = new Car();
        c1.run();
        com.jhc.test2.Car c2 = new com.jhc.test2.Car();
        c2.stop();

        Date d1 = new Date();
        System.out.println(d1);
    }

}
