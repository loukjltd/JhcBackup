package com.hziee;

public class Test02 {
    public static void main(String[] args) {
        User[] users = new User[3];

        User users2[] = {
                new User(101, "Tom"),
                new User(102, "Smith"),
                new User(103, "Lily")
        };

        users[0] = new User(1001, "ZhangSan");
        users[1] = new User(1002, "LiSi");
        users[2] = new User(1003, "WangWu");

        for(int i = 0; i < users.length; i++) {
            System.out.println(users[i]);
        }

        for(User u: users2) {
            System.out.println(u);
        }
    }
}

class User {
    private int id;
    private String name;

    public User(int id, String name) {
        this.id = id;
        this.name = name;
    }

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", name='" + name + '\'' +
                '}';
    }
}
