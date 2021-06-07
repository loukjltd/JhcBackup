import java.util.Scanner;

public class TestSystemIn {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入用户名：");
        String username = scanner.nextLine();
        System.out.print("请输入年龄：");
        int age = scanner.nextInt();
        System.out.print("请输入月薪：");
        double salary = scanner.nextDouble();
        System.out.println("==========");
        System.out.println("您的用户名为 " + username + " 。");
        System.out.println("您的年龄为 " + age + " 岁。");
        System.out.println("您的年薪为 " + salary * 12 + " 元。");
    }
}