public class TestIntDouble {
    public static void main(String[] args) {
        byte age = 18;
        short salary = 25000;
        int beijingPopulation = 30000000;
        long globalPopulation = 7000000000L;  //若需要Long类型，需手动转换，即在末尾加L

        int t010 = 65;  //十进制数
        int t008 = 065;  //八进制数
        int t016 = 0x65;  //十六进制数
        int t002 = 0b01000001;  //二进制数

        System.out.println(t010);
        System.out.println(t008);
        System.out.println(t016);
        System.out.println(t002);

        double doubleNumber = 3.14;
        float floatNumber = 3.14F;  //小数默认为Double，需手动转换为Float类型，即在末尾加F
        double doubleNumber2 = 314E-2; //科学计数法，如左侧表示314*10^(-2)

        System.out.println(doubleNumber);
        System.out.println(floatNumber);
        System.out.println(doubleNumber2);

        double doubleNumber3 = 0.01;
        float floatNumber3 = 0.01F;

        System.out.println(doubleNumber3 == floatNumber3);
    }
}