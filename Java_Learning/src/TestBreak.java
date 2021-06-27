public class TestBreak {
    public static void main(String[] args) {
        int whileCount = 0;
        while (true) {
            int whileNum = (int)(Math.random() * 100);
            System.out.println(whileNum);
            whileCount ++;
            if (whileNum == 88) {
                break;
            }
        }
        System.out.println("Total: " + whileCount);
    }
}
