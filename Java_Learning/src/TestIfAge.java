public class TestIfAge {
    public static void main(String[] args) {
        int randomAge = (int)(Math.random() * 100);
        if(randomAge <= 15) {
            System.out.println(randomAge + "岁为儿童。");
        }else if(randomAge <= 24) {
            System.out.println(randomAge + "岁为青年。");
        }else if(randomAge <= 44) {
            System.out.println(randomAge + "岁为中年。");
        }else if(randomAge <= 64) {
            System.out.println(randomAge + "岁为中老年。");
        }else {
            System.out.println(randomAge + "岁为老年。");
            if(randomAge > 85) {
                System.out.println("它还是寿星！");
            }
        }
    }
}
