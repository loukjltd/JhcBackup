import java.util.Scanner;

public class TestHeartLife {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入心跳速率：");
        long rate = scanner.nextLong();
        System.out.print("请输入活了几岁：");
        long age = scanner.nextInt();
        long totalRates = (age * 365 * 24 * 60 * 60) * rate;
        System.out.println("他的一生总共跳动了" + totalRates + "次。");
    }
}