public class TestOverload {
    public static void main(String[] args) {
    }

    public static int addNum(int num1, int num2) {
        return num1 + num2;
    }

    public static double addNum(double num1, int num2) {
        return num1 + num2;
    }

    public static int addNum(int num1, int num2, int num3) {
        return num1 + num2 + num3;
    }

    public static double addNum(int num1, double num2) {
        return num1 + num2;
    }
}
