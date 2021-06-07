public class TestIf {
    public static void main(String[] args) {
        System.out.println("随机生成[0, 1)之间的随机数为 " + Math.random());
        int randomInteger = (int)(Math.random() * 10);
        System.out.println("随机生成[0, 10)之间的随机数为 " + randomInteger);

        if(randomInteger < 5) {
            System.out.println("这个数比较小，为 " + randomInteger);
        }else {
            System.out.println("这个数比较大，为" + randomInteger);
        }
    }
}
