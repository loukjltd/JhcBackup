public class User2 {
    int user2Id;
    String user2Name;
    String user2Pwd;

    public User2() {
        System.out.println("无参数正在初始化的对象：" + this);
    }

    public User2(int user2Id, String user2Name) {
        System.out.println("有参数正在初始化的对象：" + this);
        this.user2Id = user2Id;
        this.user2Name = user2Name;

    }

    public User2(int user2Id, String user2Name, String user2Pwd) {
        this(user2Id, user2Name);
        this.user2Pwd = user2Pwd;
    }

    public void loginAccount() {
        System.out.println("即将登陆的账户是：" + this.user2Name);
        System.out.println("它的密码是：" + this.user2Pwd);
        System.out.println();
    }

    public static void main(String[] args) {
        User2 u1 = new User2();
        u1.loginAccount();

        User2 u2 = new User2(1008, "Sean");
        u2.loginAccount();

        User2 u3 = new User2(1018, "Bruce", "Guo182");
        u3.loginAccount();
    }
}
