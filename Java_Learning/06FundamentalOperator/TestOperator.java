public class TestOperator {
    public static void main(String[] args) {
        System.out.println("***算术运算符***");
        int a = 3;
        int b = 4;
        int c = (a + b) * 2;
        System.out.println(c);
        int d1 = 15 / 4;
        System.out.println(d1);
        int d2 = 15 % 4;
        System.out.println(d2);

        int x = 10;
        int y = 20;
        int z = 5;
        int l = 100;
        int m = 8;
        int n = 8;
        y = x ++; //先进行自我赋值，后自行增加
        z = ++ x; //先进行自行增加，后自我赋值
        m = l --;
        n = -- l;
        System.out.println(y);
        System.out.println(z);
        System.out.println(m);
        System.out.println(n);

        System.out.println("***扩展运算符***");
        int extendedA = 20;
        int extendedB = 30;
        extendedA += extendedB;
        System.out.println(extendedA);

        System.out.println("***关系运算符***");
        int relationA = 20;
        int relationB = 30;
        boolean relationResult = a < b;
        System.out.println(relationResult);

        System.out.println("***逻辑运算符***");
        boolean logicalA = true & false;  //fasle
        boolean logicalB = true | false;  //true
        boolean logicalC = !logicalB;  //false
        boolean logicalD = true ^ true;  //false
        System.out.println(logicalA);
        System.out.println(logicalB);
        System.out.println(logicalC);
        System.out.println(logicalD);

        boolean logicalE = 3 < 4 || (4 < 4 / 0);  //true
        System.out.println(logicalE);

        System.out.println("***位运算符***");
        int positionA = 3;
        int positionB = 7;
        System.out.println(positionA & positionB);  //3
        System.out.println(positionA | positionB);  //7
        System.out.println(positionA ^ positionB);  //4
        System.out.println(~positionB);  //-7

        int positionC = 3 << 5;  //3 * 2 * 2 * 2 * 2 * 2 = 96
        int positionD = 1000 >> 3;  //1000 / 2 / 2 / 2 = 125
        System.out.println(positionC);
        System.out.println(positionD);

        System.out.println("***字符串连接符***");
        int connectionA = 3;
        int connectionB = 4;
        System.out.println(connectionA + connectionB);
        System.out.println("The result is " + connectionA + connectionB);

        System.out.println("***条件运算符***");
        int conditionA = 30;
        int conditionB = 40;
        int minCondition = conditionA < conditionB ? conditionA : conditionB;
        System.out.println(minCondition);

    }
}