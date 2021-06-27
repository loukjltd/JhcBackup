public class TestWhile {
    public static void main(String[] args) {
        int i = 1;
        while (i <= 100) {
            System.out.println(i);
            i += 1;
        }
        int j = 1;
        int totalSum = 0;
        while (j <= 100) {
            totalSum = totalSum + j;
            j += 1;
        }
        System.out.println(totalSum);
    }
}
