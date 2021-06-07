public class TestIfLetter {
    public static void main(String[] args) {
        int randomLetterNumber = (int)(Math.random() * 26);
        char randomLetter = 'a';
        randomLetter = (char)(randomLetter + randomLetterNumber);
        if(randomLetter == 'a'|| randomLetter == 'e' || randomLetter == 'i' || randomLetter == 'o' || randomLetter == 'u') {
            System.out.println("元音字母：" + randomLetter);
        }else {
            System.out.println("辅音字母：" + randomLetter);
        }
    }
}
