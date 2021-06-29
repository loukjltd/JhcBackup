public class Student {
    // 静态特征（数据）
    int stuId;
    String stuName;
    int stuScore;
    int stuAge;

    // 方法（动态行为）（对数据的操作）
    public void someoneIsStudying() {
        System.out.println(stuName + " is studying!");
    }

    // main 方法是程序的入口
    public static void main(String[] args) {
        Student stu01 = new Student();
        stu01.stuId = 8001;
        stu01.stuName = "Tom";
        stu01.stuScore = 90;
        stu01.stuAge = 18;

        Student stu02 = new Student();
        stu02.stuId = 8002;
        stu02.stuName = "Jerry";
        stu02.stuScore = 92;
        stu02.stuAge = 28;

        Student stu03 = new Student();

        stu01.someoneIsStudying();
        stu02.someoneIsStudying();
        stu03.someoneIsStudying();
    }

}
