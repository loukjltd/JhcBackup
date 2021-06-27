import java.util.Scanner;

public class SalarySoft {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("===年薪计算小程序===");
        while (true) {
            System.out.println("请输入你的月薪：");
            int monthSalary = scanner.nextInt();
            System.out.println("请输入你一年多少个月薪资：");
            int totalMonths = scanner.nextInt();
            int totalYearSalary = monthSalary * totalMonths;
            System.out.println("您的年薪为：" + totalYearSalary + "元");

            if (totalYearSalary > 100000 && totalYearSalary <= 200000) {
                System.out.println("恭喜你超过全国 90% 的打工人！");
            } else if (totalMonths > 200000) {
                System.out.println("恭喜你超过全国 98% 的打工人！");
            }

            System.out.println("请输入你想接下去的操作：");
            int nextOperation = scanner.nextInt();
            if (nextOperation == 88) {
                break;
            } else if (nextOperation == 66){
                System.out.println("小程序正在重新启动...");
            }
        }
    }
}
