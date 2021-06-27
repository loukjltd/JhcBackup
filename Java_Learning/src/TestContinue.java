public class TestContinue {
    public static void main(String[] args) {
        int continueCount = 0;
        for (int continueNum = 100; continueNum <= 150; continueNum ++) {
            if (continueNum % 3 == 0) {
                continue;
            }
            System.out.print(continueNum + "\t");
            continueCount ++;
            if (continueCount % 5 == 0) {
                System.out.println("\t");
            }
        }

    }
}
