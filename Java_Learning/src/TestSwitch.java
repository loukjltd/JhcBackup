public class TestSwitch {
    public static void main(String[] args) {
        //switch可传入整数、枚举、字符串
        int grade = 1;
        switch (grade){
            case 1:
                System.out.println("大一");
                break;
            case 2:
                System.out.println("大二");
                break;
            case 3:
                System.out.println("大三");
                break;
            default:
                System.out.println("大四");
                break;
        }

        int month = 1;
        switch (month){
            case 1:
            case 2:
            case 3:
                System.out.println("春季");
                break;
            case 4:
            case 5:
            case 6:
                System.out.println("夏季");
                break;
            case 7:
            case 8:
            case 9:
                System.out.println("秋季");
                break;
            case 10:
            case 11:
            case 12:
                System.out.println("冬季");
                break;

        }
    }
}
