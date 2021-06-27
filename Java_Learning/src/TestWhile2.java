public class TestWhile2 {
    public static void main(String[] args) {
        for (int n = 1; n <= 10; n ++) {
            for (int m = 0; m <= 9; m ++) {
                System.out.print(m + "\t");
            }
            System.out.println("\t");
        }

        for (int c = 1; c <= 5; c ++) {
            for (int p = 0; p <= 5; p ++) {
                if (p % 2 == 0) {
                    System.out.print("Img" + "\t");
                } else {
                    System.out.print("Cnt" + "\t");
                }
            }
            System.out.println("\t");
        }
    }
}
