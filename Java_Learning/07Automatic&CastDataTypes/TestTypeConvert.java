public class TestTypeConvert {
    public static void main(String[] args) {
        //自动数据类型转换：表数范围小的可以自动转换为表数范围大的
        long a1 = 1234;
        float a2 = a1;
        System.out.println(a2);

        //整型常量可直接赋值给byte/short/char类型，只要不超过表数范围，则可以自动转换
        byte b1 = 127; //合法
        //byte b2 = 128; //不合法

        //算术运算符，两个都是整型：有一个是long，则结果为long；否则为int (即使是byte也是int)
        long c1 = 1234;
        long c2 = 123;
        long c3 = c1 + c2;

        //算术运算符，有一个是double，则结果是double
        double d1 = 3.14;
        int d2 = 3;
        double d3 = d1 * d2;

        //强制数据类型转换
        double m1 = 5.823445;
        int m2 = (int) m1;
        System.out.println(m2);
        char m3 = 'c';
        int m4 = m3 + 2;
        char m5 = (char) m4;
        System.out.println(m5);

        //若目标值超出了目标类型的表数范围，则无意义；虽然能够正确显示，但无实际意义
        long xx1 = 19999;
        byte xx2 = (byte) xx1;
        System.out.println(xx2);

        //溢出错误：当处理比较大的数据时需注意是否会溢出
        int mySalary = 1000000000;
        int passYears = 30;
        int totalSalary = mySalary * passYears;
        long realTotalSalary = 1L * mySalary * passYears; //1L*表示用于创建long类型
        System.out.println(totalSalary);
        System.out.println(realTotalSalary);
    }
}