public class TestIfGrade {
    public static void main(String[] args) {
        int randomGrade = (int)(Math.random() * 100);
        if(randomGrade < 60) {
            System.out.println("分数：" + randomGrade + "分");
            System.out.println("不及格！");
        }else if(randomGrade <= 69) {
            System.out.println("分数：" + randomGrade + "分");
            System.out.println("成绩一般！");
        }else if(randomGrade <= 79) {
            System.out.println("分数：" + randomGrade + "分");
            System.out.println("成绩良好！");
        }else if(randomGrade <= 89) {
            System.out.println("分数：" + randomGrade + "分");
            System.out.println("成绩优秀！");
        }else {
            System.out.println("分数：" + randomGrade + "分");
            System.out.println("你就是个天才！");
        }
    }
}
