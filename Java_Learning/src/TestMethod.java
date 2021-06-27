public class TestMethod {
    public static void main(String[] args) {
        int sum = addTwoNumber(100, 200);
        System.out.println(sum);
        printInfo();
        printInfo();
    }

    // 两个数求和
    public static int addTwoNumber(int num1, int num2) {
        return num1 + num2;
    }

    // 打印信息
    public static void printInfo() {
        System.out.println("Jinhua Polytechnic!");
    }
}
