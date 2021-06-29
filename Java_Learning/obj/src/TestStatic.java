public class TestStatic {
    static String companyName = "Jinhua Polytechnic";
    static int companyId = 0;

    static {
        System.out.println("类被初始化的调用");
        companyId = 18888;
    }

    static void printCompanyName() {
        System.out.println(companyName);
    }

    void loginId() {
        System.out.println("Login");
    }

    public static void main(String[] args) {
        TestStatic.printCompanyName();

        TestStatic t1 = new TestStatic();
        t1.loginId();
    }
}
