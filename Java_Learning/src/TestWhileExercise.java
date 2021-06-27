public class TestWhileExercise {
    public static void main(String[] args) {
        // 使用 for 循环，打印出 a-z 共 26 个字母。
        char letter = 'a';
        int letterCount = 1;
        for (int i = 0; i < 26; i ++) {
            System.out.println("第" + letterCount + "个字母是：" + letter);
            letter = (char) (letter + 1);
            letterCount ++;
        }

        System.out.println("\t");
        // 打印九九乘法表。
        for (int one = 1; one <= 9; one ++) {
            for (int two = 1; two <= one; two ++){
                System.out.print(one + "*" + two + "=" + one * two + "\t");
                if (two == one) {
                    System.out.println("\t");
                }
            }
        }
    }
}
