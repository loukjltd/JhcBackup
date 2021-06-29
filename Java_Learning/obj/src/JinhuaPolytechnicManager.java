public class JinhuaPolytechnicManager {
    int stuId;
    String stuName;
    int stuAge;
    Computer computer;

    void someoneIsStudying() {
        System.out.println("I am studying! The PC brand that I am using is " + computer.pcBrand + ".");
    }

    public static void main(String[] args) {
        Computer c1 = new Computer();
        c1.pcBrand = "Apple";
        c1.pcPrice = 10000;

        Computer c2 = new Computer();
        c2.pcBrand = "Lenovo";
        c2.pcPrice = 8000;

        JinhuaPolytechnicManager stu1 = new JinhuaPolytechnicManager();
        stu1.stuId = 1001;
        stu1.stuName = "Sean";
        stu1.stuAge = 21;
        stu1.computer = c1;

        JinhuaPolytechnicManager stu2 = new JinhuaPolytechnicManager();
        stu2.stuId = 1002;
        stu2.stuName = "Bruce";
        stu2.stuAge = 22;
        stu2.computer = c2;

        stu1.someoneIsStudying();
        stu2.someoneIsStudying();

    }
}
