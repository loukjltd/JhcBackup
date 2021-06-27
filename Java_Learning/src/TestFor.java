public class TestFor {
    public static void main(String[] args) {
        for (int k = 1; k <= 100; k = k + 1) {
            System.out.println(k);
        }

        int totalSum2 = 0;
        for (int l = 1; l <= 100; l = l + 1){
            totalSum2 = totalSum2 + l;
        }
        System.out.println(totalSum2);
    }
}
