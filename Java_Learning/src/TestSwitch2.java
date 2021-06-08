public class TestSwitch2 {
    public static void main(String[] args) {
        int arabianNumber = (int)(Math.random() * 10);
        char bigNumber = ' ';
        switch (arabianNumber) {
            case 0:
                bigNumber = '零';
            case 1:
                bigNumber = '壹';
                break;
            case 2:
                bigNumber = '貮';
                break;
            case 3:
                bigNumber = '叁';
                break;
            case 4:
                bigNumber = '肆';
                break;
            case 5:
                bigNumber = '伍';
                break;
            case 6:
                bigNumber = '陆';
                break;
            case 7:
                bigNumber = '柒';
                break;
            case 8:
                bigNumber = '扒';
                break;
            case 9:
                bigNumber = '玖';
                break;
        }
        System.out.println("阿拉伯数字 " + arabianNumber + " 的大写数字为 " + bigNumber);
    }
}
